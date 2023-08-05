from cleo import option

from poetry.utils._compat import Path

from .command import Command


class PublishCommand(Command):

    name = "publish"
    description = "Publishes a package to a remote repository."

    options = [
        option(
            "repository", "r", "The repository to publish the package to.", flag=False
        ),
        option("username", "u", "The username to access the repository.", flag=False),
        option("password", "p", "The password to access the repository.", flag=False),
        option(
            "cert", None, "Certificate authority to access the repository.", flag=False
        ),
        option(
            "client-cert",
            None,
            "Client certificate to access the repository.",
            flag=False,
        ),
        option("build", None, "Build the package before publishing."),
        option("dry-run", None, "Perform all actions except upload the package."),
    ]

    help = """The publish command builds and uploads the package to a remote repository.

By default, it will upload to PyPI but if you pass the --repository option it will
upload to it instead.

The --repository option should match the name of a configured repository using
the config command.
"""

    loggers = ["poetry.masonry.publishing.publisher"]

    def handle(self):
        from poetry.publishing.publisher import Publisher

        publisher = Publisher(self.poetry, self.io)

        # Building package first, if told
        if self.option("build"):
            if publisher.files:
                if not self.confirm(
                    "There are <info>{}</info> files ready for publishing. "
                    "Build anyway?".format(len(publisher.files))
                ):
                    self.line_error("<error>Aborted!</error>")

                    return 1

            self.call("build")

        files = publisher.files
        if not files:
            self.line_error(
                "<error>No files to publish. "
                "Run poetry build first or use the --build option.</error>"
            )

            return 1

        self.line("")

        cert = Path(self.option("cert")) if self.option("cert") else None
        client_cert = (
            Path(self.option("client-cert")) if self.option("client-cert") else None
        )

        publisher.publish(
            self.option("repository"),
            self.option("username"),
            self.option("password"),
            cert,
            client_cert,
            self.option("dry-run"),
        )

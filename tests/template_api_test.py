from cobbler.template_api import CobblerTemplate


class TestCobblerTemplate:
    def test_compile(self):
        # Arrange

        # Act
        result = CobblerTemplate().compile()

        # Assert
        assert False

    def test_read_snippet_none(self):
        # Arrange
        test_template = CobblerTemplate()

        # Act
        result = test_template.read_snippet("nonexistingsnippet")

        # Assert
        assert result is None

    def test_read_snippet(self):
        # Arrange
        test_template = CobblerTemplate()

        # Act
        result = test_template.read_snippet()

        # Assert
        assert False


    def test_SNIPPET(self):
        # Arrange
        test_template = CobblerTemplate()

        # Act
        # Assert
        assert False

    def test_sedesc(self):
        # Arrange
        test_input = "This () needs [] to ^ be * escaped {}."
        expected = "This \\(\\) needs \\[\\] to \\^ be \\* escaped \\{\\}."
        test_template = CobblerTemplate()

        # Act
        result = test_template.sedesc(test_input)

        # Assert
        assert result == expected

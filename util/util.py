class Util:

    @staticmethod
    def object_to_json(obj):
        pass

    @staticmethod
    def json_to_object(json):
        pass

    @staticmethod
    def check_email_pattern(email) -> None:
        """
        emails should end with the domain “@university.com”,
        hence firstname.lastname@university.com is a valid email,
        while firstname.lastname@university is not

        :param email:
        :return:
        """
        # TODO
        pass

    @staticmethod
    def check_password_pattern(password):
        """
        A password is considered valid if it meets the following criteria:
            (i) It starts with an upper-case character,
            (ii) It contains at least five (5) letters,
            (iii) It is followed by three (3) or more digits.
        :param password:
        :return:
        """
        # TODO
        pass

    @staticmethod
    def encode_md5(content) -> str:
        """
        encode content by using md5
        :param content: text-based content
        :return: md5 hex hash value with 32-digit value.
        """
        # TODO
        md5_value = ""
        return md5_value
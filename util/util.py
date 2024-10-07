class Util:

    @staticmethod
    def object_to_json(obj):
        pass

    @staticmethod
    def json_to_object(json):
        pass

    @staticmethod
    def check_pattern(email, password) -> bool:

        # 1: check parameters to find whether they meet the pattern requirements.
        #   please call Util.check_email_pattern to check whether email is valid.
        #   please call Util.check_password_pattern to check whether password is valid
        ret1 = Util.check_email_pattern(email)
        ret2 = Util.check_password_pattern(password)

        # 2 encapsulate result of combination of ret1 and ret2
        ret = ret1 and ret2
        if ret:
            print("Email and password formats acceptable.")
        else:
            print("Incorrect email or passport format.")

        return ret

    @staticmethod
    def check_email_pattern(email) -> bool:
        """
        emails should end with the domain “@university.com”,
        hence firstname.lastname@university.com is a valid email,
        while firstname.lastname@university is not

        :param email
        :return:    True: meet pattern
                    False(default value): don't meet pattern
        """
        # TODO
        return False

    @staticmethod
    def check_password_pattern(password) -> bool:
        """
        A password is considered valid if it meets the following criteria:
            (i) It starts with an upper-case character,
            (ii) It contains at least five (5) letters,
            (iii) It is followed by three (3) or more digits.
        :param password
        :return: True:  meet pattern
                 False: don't meet pattern
        """
        # TODO
        return False

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
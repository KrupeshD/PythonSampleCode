"""
This is just a sample code. Not functional.
It highlights how simple factory class can be implemented to create object based on parameter passed

Factory is not a design pattern by itself; rather it serves as a basis for several design pattern such as:
Factory Method and Abstract Factory
"""
class SimpleFactory(object):
    @staticmethod
    #staticmethod is a decorator which allows to call the method without class instance #
    def build_connection(protocol):
        if protocol == 'http':
            return HTTPConnection()
        elif protocol =='ftp':
            return FTPConnection()

        else:
            raise RuntimeError('Unknown Protocol')

if __name__ == '__main__':
    protocol = raw_input('Which Protocol to use? (http or ftp): ')
    protocol = SimpleFactory.build_connection(protocol)
    protocol.connect()
    print(protocol.get_response())


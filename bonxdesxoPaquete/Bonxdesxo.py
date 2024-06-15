class Bonxdesxo:
    def __init__(self, descodigo=None, boncodigo=None, bonxdescodigo=None, bonxdesvalor=None):
        self._descodigo = descodigo
        self._boncodigo = boncodigo
        self._bonxdescodigo = bonxdescodigo
        self._bonxdesvalor = bonxdesvalor

    def __str__(self):
        return f'''
            DESCODIGO: {self._descodigo}, BONCODIGO: {self._boncodigo},
            BONXDESCODIGO: {self._bonxdescodigo}, BONXDESVALOR: {self._bonxdesvalor}
        '''

    @property
    def descodigo(self):
        return self._descodigo

    @descodigo.setter
    def descodigo(self, descodigo):
        self._descodigo = descodigo

    @property
    def boncodigo(self):
        return self._boncodigo

    @boncodigo.setter
    def boncodigo(self, boncodigo):
        self._boncodigo = boncodigo

    @property
    def bonxdescodigo(self):
        return self._bonxdescodigo

    @bonxdescodigo.setter
    def bonxdescodigo(self, bonxdescodigo):
        self._bonxdescodigo = bonxdescodigo

    @property
    def bonxdesvalor(self):
        return self._bonxdesvalor

    @bonxdesvalor.setter
    def bonxdesvalor(self, bonxdesvalor):
        self._bonxdesvalor = bonxdesvalor

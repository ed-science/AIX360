import os
import requests

class dwnld_CEM_MAF_celebA():
    '''
    Class with functions to download
        1. celebA prediction model
        2. celebA attribute functions
        3. celebA data files
    '''
        
    def dwnld_celebA_attributes(self, local_path, attributes):
        '''
        Download celebA attribute functions
        
        Args:
            local path (str): local path to where files are downloaded
            attributes (str list): list of attributes to download attribute functions for 

        Returns:
            files (str list): list of files that were downloaded
        '''

        # This is the link where attribute functions are stored
        cdcweb = 'http://aix360.mybluemix.net/static/CEM-MAF/attr_model/'

        # Next build list of files to download
        cdcfiles = []
        for attr in attributes:
            cdcfiles.extend(
                (
                    f'simple_{attr}.ckpt',
                    f'simple_{attr}_model.json',
                    f'simple_{attr}_weights.h5',
                )
            )

        files = []

        for f in cdcfiles:
            file = requests.get(os.path.join(cdcweb, f), allow_redirects=True)
            open(os.path.join(local_path, f), 'wb').write(file.content)

        # r=root, d=directories, f = files
        for r, d, f in os.walk(local_path):
            for attr in attributes:
                files.extend(os.path.join(r, file) for file in f if attr in file)
        print('Attribute files downloaded:')
        print(files)

        return files
        
    def dwnld_celebA_model(self, local_path):
        '''
        Download celebA model
        
        Args:
            local path (str): local path to where files are downloaded

        Returns:
            files (str list): list of files that were downloaded
        '''

        # This is the link where the celebA model is stored
        cdcweb = 'http://aix360.mybluemix.net/static/CEM-MAF/celebA'

        files = []

        file = requests.get(cdcweb, allow_redirects=True)
        open(os.path.join(local_path, 'celebA'), 'wb').write(file.content)

        # r=root, d=directories, f = files
        for r, d, f in os.walk(local_path):
            files.extend(os.path.join(r, file) for file in f if file == 'celebA')
        print('celebA model file downloaded:')
        print(files)

        return files
 
    def dwnld_celebA_data(self, local_path, ids):
        '''
        Download celebA data files
        
        Args:
            local path (str): local path to where files are downloaded
            ids (int list): list of ids to download data for 
        
        Returns:
            files (str list): list of files that were downloaded
        '''

        # This is the link where celebA image data is stored
        cdcweb = 'http://aix360.mybluemix.net/static/CEM-MAF/data/'

        # Next build list of files to download
        cdcfiles = []
        for id in ids:
            cdcfiles.extend(
                (
                    f'{str(id)}_img.npy',
                    f'{str(id)}_latent.npy',
                    f'{str(id)}img.png',
                )
            )

        files = []

        if not os.path.exists(local_path):
            os.makedirs(local_path)

        for f in cdcfiles:
            file = requests.get(os.path.join(cdcweb, f), allow_redirects=True)
            open(os.path.join(local_path, f), 'wb').write(file.content)

        # r=root, d=directories, f = files
        for r, d, f in os.walk(local_path):
            for id in ids:
                files.extend(os.path.join(r, file) for file in f if str(id) in file)
        print('Image files downloaded:')
        print(files)

        return files

import pandas as pd 
from logger.log import logger

def load_data(path, cols, separator=';', index='id'):
    try:
        # dtf.set_index('id').to_dict('index')
        data = pd.read_csv(path, sep=separator, usecols=cols)
        return data.set_index(index).to_dict('index')
    except Exception as e:
        logger.error('Erreur => {}'.format(e))
        return None

def get_root(all_data):
    return list(filter(lambda item: item['idParent'] == 0 , all_data.values()))

def merge_data(root, all_data):
    return None

if __name__ == '__main__':
    logger.info("running......")
    structures = load_data('source_data/structures.csv', ['id', 'idParent', 'nom', 'adresse'] )
    postes = load_data('source_data/postes.csv', ['id', 'idStructure', 'nom', 'nombreDesire'] )
    print(get_root(structures))


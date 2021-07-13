DEVICE = 3
LOCAL_TEMP_FOLDER = 'temp'
DELETE_TEMP_FILES = True

MODEL_PATHS = {
    'token-single_oov': {'model': 'data/token.char_lstm.ft_oov_tok.44_seed.146.model',
                         'dset': 'data/token.char_lstm.ft_oov_tok.44_seed.dset',
                         'gpu': 'False'},
    'token-single': {'model': 'data/token.char_cnn.ft_tok.46_seed.104.model',
                     'dset': 'data/token.char_cnn.ft_tok.46_seed.dset',
                     'gpu': 'False'},
    'token-multi_oov': {'model': 'data/multitok.char_cnn.ft_oov_tok.48_seed.123.model',
                        'dset': 'data/multitok.char_cnn.ft_oov_tok.48_seed.dset',
                        'gpu': 'False'},
    'token-multi': {'model': 'data/multitok.char_cnn.ft_tok.52_seed.173.model',
                    'dset': 'data/multitok.char_cnn.ft_tok.52_seed.dset',
                    'gpu': 'False'},
    'morph_oov': {'model': 'data/morph.char_cnn.ft_oov_yap.49_seed.87.model',
                  'dset': 'data/morph.char_cnn.ft_oov_yap.49_seed.dset',
                  'gpu': 'False'},
    'morph': {'model': 'data/morph.char_cnn.ft_yap.50_seed.80.model',
              'dset': 'data/morph.char_cnn.ft_yap.50_seed.dset',
              'gpu': 'False'}
}
MULTI_MODEL_FOR_HYBRID = 'token-multi'

YAP_PATH = '../yapproj/src/yap/yap'

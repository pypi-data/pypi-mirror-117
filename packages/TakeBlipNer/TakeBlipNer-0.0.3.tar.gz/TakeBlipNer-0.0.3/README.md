# BiLSTM-CRF on PyTorch #

An efficient BiLSTM-CRF implementation that leverages mini-batch operations on multiple GPUs.

Tested on the latest PyTorch Version (0.3.0) and Python 3.5+.

The latest training code utilizes GPU better and provides options for data parallization across multiple GPUs using `torch.nn.DataParallel` functionality.

## Requirements ##

Install all required packages (other than pytorch) from `requirements.txt`

    pip install -r requirements.txt

Optionally, standalone tensorboard can be installed from `https://github.com/dmlc/tensorboard` for visualization and plotting capabilities.

## Our Training ##
For local execution run command:

    python train.py --input-path files/input/ner_sample.csv --sentence_column MessageProcessed --label_column NER --postag_model_path postag/model.pkl --postag_label_path postag/vocab-label.pkl --save-dir files/output/ --wordembed-path files/input/titan_v2_after_correction_fasttext_window4_mincount20_cbow.kv --epochs 5 --bidirectional --word-dim 300 --separator , 

    python train.py --input-path files/input/ner_sample.csv --sentence_column MessageProcessed --label_column NER --postag_model_path postag/model.pkl --postag_label_path postag/vocab-label.pkl --save-dir files/output/ --wordembed-path files/input/titan_v2_after_correction_fasttext_window4_mincount20_cbow.kv --epochs 5 --bidirectional --word-dim 300 --separator , --val --val-path files/input/ner_validation.csv --val-period 1e 
    
    python train.py --input-path files/input/ner_sample.csv --sentence_column MessageProcessed --label_column NER --postag_model_path postag/model.pkl --postag_label_path postag/vocab-label.pkl --save-dir files/output/ --wordembed-path files/input/titan_v2_after_correction_fasttext_window4_mincount20_cbow.kv --epochs 5 --bidirectional --word-dim 300 --separator , --val --val-path files/input/ner_validation.csv --val-period 1e --max-decay-num 2 --max-patience 2 --learning-rate-decay 0.1 --patience-threshold 0.98


For running on Google Colab:

    !python train.py --input-path 'files/input/ner_sample.csv' --separator ',' --sentence_column 'MessageProcessed' --label_column 'NER' --postag_model_path postag/model.pkl --postag_label_path postag/vocab-label.pkl --save-dir 'files/output/' --wordembed-path '/content/gdrive/Shared drives/Data & Analytics/D&A Research/TKS/Modelos/Embedding/FastText/Q3 fasttext/titan_v2_after_correction_fasttext_window4_mincount20_cbow.kv' --epochs 5  --word-dim 300  --bidirectional 

    !python train.py --input-path 'files/input/ner_sample.csv' --separator ',' --sentence_column 'MessageProcessed' --label_column 'NER' --postag_model_path postag/model.pkl --postag_label_path postag/vocab-label.pkl --save-dir 'files/output/' --wordembed-path '/content/gdrive/Shared drives/Data & Analytics/D&A Research/TKS/Modelos/Embedding/FastText/Q3 fasttext/titan_v2_after_correction_fasttext_window4_mincount20_cbow.kv' --epochs 5 --val --val-path files/input/ner_validation.csv --word-dim 300  --bidirectional --val-period 1e 
    
	!python train.py --input-path 'files/input/ner_sample.csv' --separator ',' --sentence_column 'MessageProcessed' --label_column 'NER' --postag_model_path postag/model.pkl --postag_label_path postag/vocab-label.pkl --save-dir 'files/output/' --wordembed-path '/content/gdrive/Shared drives/Data & Analytics/D&A Research/TKS/Modelos/Embedding/FastText/Q3 fasttext/titan_v2_after_correction_fasttext_window4_mincount20_cbow.kv' --epochs 5 --val --val-path files/input/ner_validation.csv --word-dim 300  --bidirectional --val-period 1e --max-decay-num 2 --max-patience 2 --learning-rate-decay 0.1 --patience-threshold 0.98
    	
## Training ##

Prepare data first. Data must be supplied in one csv file where the first column contain the sentences and the second one the respective labels for that sentence. File might be prepared as follows:

    (sample.csv)
	MessageProcessed,					Tags
    the fat rat sat on a mat,	det adj noun verb prep det noun
    the cat sat on a mat,		det noun verb prep det noun
    ...,						...
    
Then the above input is provided to `train.py` using `--input-path` and the column name for the sentences and the labels using `--sentence_column` and `--label_column`.

    python train.py --input-path files/input/sample.csv --sentence_column MessageProcessed --label_column Tags ...

You might need to setup several more parameters in order to make it work. Checkout `examples/atis` for an example of training a simple BiLSTM-CRF model with ATIS dataset. Run `python preprocess.py` at the example directory to convert to the dataset to`train.py`-friendly format, then run 

    python ../../train.py --config train-atis.yml`
 
 to see a running example. The example configuration assumes that standalone tensorboard is installed (you could turn it off in the configuration file).
 
 For more information on the configurations, check out `python train.py --help`.

## Prediction ##
For local execution run command for  one line prediction:
    
    python predict.py --model-path files/output/model.pkl --input-sentence "frase para prever" --ner-label-vocab files/output/vocab_label.pkl --postag-model-path postag/model.pkl --postag-label-vocab postag/vocab-label.pkl --save-dir files/output/pred.csv --wordembed-path files/input/titan_v2_after_correction_fasttext_window4_mincount20_cbow.kv
    
For local execution run for batch prediction:
    
    python predict.py --model-path files/output/model.pkl --input-path files/input/sample_predict.csv --sentence-column MessageProcessed --ner-label-vocab files/output/vocab_label.pkl --postag-model-path postag/model.pkl --postag-label-vocab postag/vocab-label.pkl --save-dir files/output/pred.csv --wordembed-path files/input/titan_v2_after_correction_fasttext_window4_mincount20_cbow.kv --separator ,

For Google colab execution run command for batch prediction:
    
    !python predict.py --model-path files/output/model.pkl --input-path files/input/sample_predict.csv --separator "," --sentence-column MessageProcessed --ner-label-vocab files/output/vocab_label.pkl --postag-model-path postag/model.pkl --postag-label-vocab postag/vocab-label.pkl --save-dir files/output/pred.csv --wordembed-path '/content/gdrive/Shared drives/Data & Analytics/D&A Research/TKS/Modelos/Embedding/FastText/Q3 fasttext/titan_v2_after_correction_fasttext_window4_mincount20_cbow.kv'
    
For Google colab execution run command for one line prediction:
    
     !python predict.py --model-path files/output/model.pkl --input-sentence "frase para prever" --ner-label-vocab files/output/vocab_label.pkl --postag-model-path postag/model.pkl --postag-label-vocab postag/vocab-label.pkl --save-dir files/output/pred.csv --wordembed-path '/content/gdrive/Shared drives/Data & Analytics/D&A Research/TKS/Modelos/Embedding/FastText/Q3 fasttext/titan_v2_after_correction_fasttext_window4_mincount20_cbow.kv'
    
Data must be supplied in one csv file with one column which contain the sentences. File might be prepared as follows:

    (sample.csv)
	MessageProcessed
    the fat rat sat on a mat
    the cat sat on a mat
    ...,		
  			
## Evaluation ##

`TODO`

import os

import joblib
import whois

import features_extraction
import sys
import numpy as np

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdout.reconfigure(encoding='utf-8')


def get_prediction_from_url(test_url, domain):
    features_test = features_extraction.main(test_url, domain)
    features_test = np.array(features_test).reshape((1, -1))
    clf = joblib.load(ROOT_DIR+'ml/classifier/random_forest.pkl')
    pred = clf.predict(features_test)
    return int(pred[0])


def main():
    try:
        url = sys.argv[1]
        domain = whois.extract_domain(url)
        prediction = get_prediction_from_url(url, domain)
        if prediction == 1:
            print("SAFE")
            exit(1)
        elif prediction == -1:
            print("PHISHING")
            exit(-1)
    except Exception as e:
        print(f'EXCEPTION: {e}')
        exit(0)


if __name__ == "__main__":
    main()

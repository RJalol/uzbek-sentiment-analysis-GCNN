import os
import requests

def download_file(url: str, save_path: str):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    print(f"Downloading from {url} …")
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    with open(save_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Saved to {save_path}")

if __name__ == "__main__":
    # URLs
    url_train = "https://huggingface.co/datasets/alexcadillon/SemEval2014Task4/resolve/main/SemEval'14-ABSA-TrainData_v2%20%26%20AnnotationGuidelines/Restaurants_Train_v2.xml"
    url_test = "https://huggingface.co/datasets/alexcadillon/SemEval2014Task4/resolve/main/ABSA_Gold_TestData/Restaurants_Test_Gold.xml"

    # Save paths — loyihaning yuqori darajasidagi papka ichida
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    train_save_path = os.path.join(base_dir, "SemEval2014Task4", "Restaurants_Train_v2.xml")
    test_save_path = os.path.join(base_dir, "SemEval2014Task4", "Restaurants_Test_Gold.xml")

    download_file(url_train, train_save_path)
    download_file(url_test, test_save_path)

    print("Downloads completed.")

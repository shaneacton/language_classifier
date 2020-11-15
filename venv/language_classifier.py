import csv


def read_data():
    raw_text_lines=[]
    counter=0
    all_text_lines=[]
    with open("lang_data.csv", encoding="mbcs") as csv_file:
        all_text_lines=csv_file.readlines()[1:]
    all_text_lines=[x.strip("\n") for x in all_text_lines]
    print([x for x in all_text_lines if (x.count(",English")==0 and x.count(",Afrikaans")==0 and x.count(",Nederlands")==0)]) #we know that the last word will always be a correct label
    





def main():
    read_data()


main()
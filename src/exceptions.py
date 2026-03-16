import pandas as pd
def exceptions(Act):
 df = pd. read_excel("data/combined_df.excel")
 exceptions_dict = {}

 for act in df["Act"].unique():

    exceptions = df[
        (df["Act"] == act) & (df["section_type"] == "exception")
    ]

    exception_text = "\n\n".join(
        exceptions["section_title"] + ". " + exceptions["section_text"]
    )

    exceptions_dict[act] = exception_text

 return exceptions_dict[Act]

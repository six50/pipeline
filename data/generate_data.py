from pathlib import Path

from eu_referendum.electoral_commission.results.scripts import retrieve as eu_retrieve
from general_election.electoral_commission.results.scripts import (
    process_2010,
    process_2015,
    retrieve_2010,
    retrieve_2015,
)
from model.scripts import process as model_process

if __name__ == "__main__":

    #  Retrieve EU Referendum data
    eu_path = Path(".") / "data" / "eu_referendum" / "electoral_commission" / "results"
    eu_retrieve.main(eu_path)

    # Retrieve & clean general election data
    ge_path = Path(".") / "data" / "general_election" / "electoral_commission" / "results"
    retrieve_2010.main(ge_path)
    # retrieve_2015.main(ge_path)  # TODO: This is broken.
    # process_2010.main(ge_path)  # TODO: This is broken.
    # process_2015.main(ge_path)  # TODO: This is broken.

    # Process data ready for modelling
    model_path = Path(".") / "data"
    # model_process.main(model_path)  # TODO: This is broken.

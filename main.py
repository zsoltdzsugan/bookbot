import sys
import logging
import functions

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(args):
    logger.info("Bookbot starting...")

    file = args.filename
    with open(file) as f:
        file_contents = f.read()

        if args.count_words:
            words = functions.count_words(file_contents)
            print(f"The number of words in the document: {words}")
            
        if args.count_chars:
            char_dict = functions.count_characters(file_contents)
            print(char_dict)

        if args.print_report:
            functions.print_report(file_contents)
    
    logger.info("Bookbot shutting down...")


if __name__ == '__main__':
    args = functions.init_parser()

    try:
        main(args)
    except Exception as e:
        logger.info("An error occured during execution")
        sys.exit(1)
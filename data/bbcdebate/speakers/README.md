# BBC Debate Speaker Log

If you have any questions about these datasets please [contact us @SixFiftyData](https://twitter.com/SixFiftyData) on Twitter.

## Licence
This data is provided under a [CC-BY-SA license](https://creativecommons.org/licenses/by-sa/3.0/). This means you are free to reuse the data for any reason, as long as you give attribution to "SixFifty.org.uk" and any reuse is shared under the same licence.

## 31st May 2017 BBC Debate Speaker Log
The following dataset is available for download from this repo:

| Column | Type | Description |
| -- | -- | -- |
| `timestamp` | string | Timestamp when speaker started speaking in format `%Y-%m-%d %H:%M:%S` starting at 31st May 2017 1930 BST |
| `party` | string | Party name of speaker, e.g. `Conservatives`, `Labour`, can be blank for chair Mishal Husain |
| `speaker` | string | Name of speaker, e.g. `Mishal Husain`, `Caroline Lucas` |
| `section` | string | Section of debate, e.g. `Opening credits`, `Question 1 - Living standards` |
| `counter` | float | Number of integer seconds that this person is dominant speaker (i.e. until interrupted or has finished speaking) |
| `time_elapsed` | float | Seconds elapsed since start of debate |

## Scripts
This repo contains two scripts:

1. `debate_logger.py` is an extremely simple (~6 lines of code) script for timestamping text records and writing these to a CSV file. This was used to log who was speaking at each time using simple shorthand codes e.g. `l`, `c` for Labour/Conservative, as well as section/question markers.

2. `process_debate_log.py` processes this into the clean dataset documented above.

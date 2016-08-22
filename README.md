# Lex
Lex processes ordered text using Markov chains and multi-lexeme walks. Currently Lex is designed to process chat logs.

## To run

- Download the repository, then save any text file as `source.txt`.
- Run `gen.py` to generate weight values.
- Run `main.py > file.out` to generate text

For more info see the [wiki](https://github.com/incogn/Lex/wiki/Lex)

### Versions

`v1.0.0`<br>
Added basic text processing ability

####Future Improvements
- Make text walking less random
- Multi-sentence walks, for greater overall coherence
- Adaptation into chatbot LexBot, including
  - Self-regulating messages with appropriate timing and length
  - Response recognition and processing capability
  - Improved text processing methods

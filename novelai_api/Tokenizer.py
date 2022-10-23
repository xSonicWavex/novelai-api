from pathlib import Path
import tokenizers

from novelai_api.Preset import Model

from typing import List

tokenizers_path = Path(__file__).parent / "tokenizers"


class Tokenizer:
    """
    Abstraction of the tokenizer behind each Model
    """

    _tokenizers_name = {
        # Model.Calliope:     "gpt2",
        Model.Sigurd:       "gpt2",
        Model.Euterpe:      "gpt2",
        Model.Krake:        "pile",

        Model.Snek:         "gpt2",
        Model.Genji:        "gpt2-genji",

        Model.HypeBot:      "gpt2",
        Model.Inline:       "gpt2",
    }

    @classmethod
    def get_tokenizer_name(cls, model: Model) -> str:
        return cls._tokenizers_name[model]

    _GPT2_PATH = tokenizers_path / "gpt2_tokenizer.json"
    _GPT2_TOKENIZER = tokenizers.Tokenizer.from_file(str(_GPT2_PATH))

    _GENJI_PATH = tokenizers_path / "gpt2-genji_tokenizer.json"
    _GENJI_TOKENIZER = tokenizers.Tokenizer.from_file(str(_GENJI_PATH))

    _PILE_PATH = tokenizers_path / "pile_tokenizer.json"
    _PILE_TOKENIZER = tokenizers.Tokenizer.from_file(str(_PILE_PATH))

    _tokenizers = {
        "gpt2":             _GPT2_TOKENIZER,
        "gpt2-genji":       _GENJI_TOKENIZER,
        "pile":             _PILE_TOKENIZER,
    }

    @classmethod
    def decode(cls, model: Model, o: List[int]) -> str:
        tokenizer_name = cls._tokenizers_name[model]

        return cls._tokenizers[tokenizer_name].decode(o)

    @classmethod
    def encode(cls, model: Model, o: str) -> List[int]:
        tokenizer_name = cls._tokenizers_name[model]

        return cls._tokenizers[tokenizer_name].encode(o).ids

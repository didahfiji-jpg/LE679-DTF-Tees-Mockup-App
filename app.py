"""DTF Tees Mockup App - Windows desktop wrapper."""
import sys
from pathlib import Path
import webview


def resource_path(filename: str) -> Path:
    root = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return root / filename


if __name__ == "__main__":
    html = resource_path("index.html")
    if not html.is_file():
        raise FileNotFoundError(f"Missing bundled application file: {html}")
    webview.create_window(
        "DTF Tees Mockup App V1",
        html.resolve().as_uri(),
        width=1440,
        height=900,
        min_size=(1000, 650),
        background_color="#090c18",
    )
    webview.start(gui="edgechromium")

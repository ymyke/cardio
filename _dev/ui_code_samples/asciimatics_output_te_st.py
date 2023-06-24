import time
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.renderers import StaticRenderer
from uniseg.graphemecluster import grapheme_clusters


def show_text(screen: Screen, pos, text: str) -> None:
    Print(
        screen=screen, renderer=StaticRenderer(images=[text]), x=pos[0], y=pos[1]
    ).update(0)


what = "[nok: ✌️❤️🛡️ ok: 🍀💓🔥]"
clusters = list(grapheme_clusters(what))
clustered = ",".join(clusters)

screen = Screen.open(unicode_aware=True)
show_text(screen, (0, 0), what)
show_text(screen, (0, 1), clustered)
for i, cluster in enumerate(clusters):
    show_text(screen, (0 + i, 2), cluster)
screen.refresh()
time.sleep(10)
screen.close()

print(what)
print(clustered)
for cluster in clusters:
    print(cluster, end="")

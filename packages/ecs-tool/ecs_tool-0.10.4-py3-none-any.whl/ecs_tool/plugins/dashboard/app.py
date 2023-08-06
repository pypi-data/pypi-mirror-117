from textual import events
from textual.app import App
from textual.widgets import Placeholder


class EcsToolApp(App):
    async def on_mount(self, event: events.Mount) -> None:
        """Make a simple grid arrangement."""

        grid = await self.view.dock_grid(edge="left", size=70, name="left")

        grid.add_column(fraction=1, name="left", min_size=20)
        grid.add_column(size=30, name="center")
        grid.add_column(fraction=1, name="right")

        grid.add_row(fraction=1, name="top", min_size=2)
        grid.add_row(fraction=2, name="middle")
        grid.add_row(fraction=1, name="bottom")

        grid.add_areas(
            area1="left,top",
            area2="center,middle",
            area3="left-start|right-end,bottom",
            area4="right,top-start|middle-end",
        )

        grid.place(
            area1=Placeholder(name="area1"),
            area2=Placeholder(name="area2"),
            area3=Placeholder(name="area3"),
            area4=Placeholder(name="area4"),
        )

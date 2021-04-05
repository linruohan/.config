from flexx import flx, app


class Example(flx.Widget):

    def init(self):
        with flx.HSplit():
            flx.Button(text="foo")
            with flx.VBox():#纵向布局
                flx.Widget(style='background:red', flex=1)
                flx.Widget(style='background:blue', flex=1)
            with flx.HBox():#水平布局
                flx.Button(text='hello', flex=1)
                flx.Button(text='world', flex=2)


if __name__ == "__main__":
    main = app.launch(Example)
    app.run()

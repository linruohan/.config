from flexx import flx,app


class Example(flx.Widget):

    name = flx.StringProp('John Doe', settable=True)
    age = flx.IntProp(22, settable=True)

    @flx.action
    def increase_age(self):
        self._mutate_age(self.age + 1)

    def _create_dom(self):
        # Use this method to create a root element for this widget.
        # If you just want a <div> you don't have to implement this.
        return flx.create_element('div')  # the default is <div>

    def _render_dom(self):
        # Use this to determine the content. This method may return a
        # string, a list of virtual nodes, or a single virtual node
        # (which must match the type produced in _create_dom()).
        return [flx.create_element('span', {},
                                   'Hello', flx.create_element('b', {}, self.name), '! '),
                flx.create_element('span', {},
                                   'I happen to know that your age is %i.' % self.age),
                flx.create_element('br'),
                flx.create_element('button', {'onclick': self.increase_age},
                                   'Next year ...')
                ]
if __name__ == "__main__":
    main=app.launch(Example)
    app.run()
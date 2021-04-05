from flexx import flx,app


class Person(flx.JsComponent):  # Lives in Js
    name = flx.StringProp(settable=True)
    age = flx.IntProp(settable=True)

    @flx.action
    def increase_age(self):
        self._mutate_age(self.age + 1)


class PersonDatabase(flx.PyComponent):  # Lives in Python
    persons = flx.ListProp()

    @flx.action
    def add_person(self, name, age):
        with self:  # new components need a session
            p = Person(name=name, age=age)
        self._mutate_persons([p], 'insert', 99999)

    @flx.action
    def new_year(self):
        for p in self.persons:
            p.increase_age()


main = app.launch(PersonDatabase)
app.run()  # enter the mainloop

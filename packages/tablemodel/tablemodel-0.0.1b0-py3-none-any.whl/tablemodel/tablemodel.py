from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session


class TableModel:
    def __init__(self, schema, engine_url, table_name="main"):
        s = f"class {table_name}(SQLModel, table=True):\n"
        for v in schema:
            attribute_name = v[0]
            attribute_type = str(v[1].__name__)
            try:
                attribute_optional = v[2]
            except:
                attribute_optional = False
            try:
                attribute_pk = v[3]
            except:
                attribute_pk = False

            s += f"    {attribute_name}: "
            if attribute_optional:
                if attribute_pk:
                    s += f"Optional[{attribute_type}] = Field(default=None, primary_key={attribute_pk})"
                else:
                    s += f"Optional[{attribute_type}] = None"
            else:
                s+=attribute_type
            s+="\n"
        exec(s)
        exec(f"self._table= {table_name}")
        exec(f"self.Config= {table_name}.Config")
        exec(f"self.engine = create_engine('{engine_url}')")
        exec("SQLModel.metadata.create_all(self.engine)")

    def insert_many(self, records):
        with Session(self.engine) as session:
            [session.add(record) for record in records]
            session.commit()

    def new(self, *args, **kwargs):
        return self._table(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self._table(*args, **kwargs)

    def __getitem__(self, item):
        result = self._table[item]
        if isinstance(result, type(self._table)):
            result = TableModel(result)
        return result

    def __getattr__(self, item):
        result = getattr(self._table, item)
        if callable(result):
            result = TableModel(result)
        return result

    def __repr__(self):
        return repr(self._table)


if __name__=="__main__":
    schema = [
        ("id", int, True, True),
        ("name", str),
        ("secret_name", str),
        ("age", int, True, None)
    ]

    table = TableModel(table_name="main",
                       schema=schema,
                       engine_url="sqlite:///database.db")
    record = table(name="Deadpond", secret_name="Dive Wilson")
    table.insert_many([record])


from simpleai.search import CspProblem, backtrack

def constraint_func(names, values):
    return values[0] != values[1]  # dua simpul tidak boleh punya warna yang sama

if __name__ == "__main__":

    names = (
        'Fajar',
        'Intan',
        'Yoga',
        'Ghina',
        'Nurpia',
        'Istajib',
        'Sigit',
        'Ilmi',
        'Najwa',
        'Nesa'
    )

    colors = dict(
        (name, ['red', 'green', 'blue', 'gray'])
        for name in names
    )

    constraints = [

        (('Fajar', 'Intan'), constraint_func),
        (('Fajar', 'Yoga'), constraint_func),

        (('Intan', 'Yoga'), constraint_func),
        (('Intan', 'Ghina'), constraint_func),
        (('Intan', 'Najwa'), constraint_func),
        (('Intan', 'Nurpia'), constraint_func),

        (('Yoga', 'Ghina'), constraint_func),
        (('Yoga', 'Ilmi'), constraint_func),
        (('Yoga', 'Sigit'), constraint_func),

        (('Ghina', 'Sigit'), constraint_func),
        (('Ghina', 'Istajib'), constraint_func),
        (('Ghina', 'Najwa'), constraint_func),

        (('Nurpia', 'Najwa'), constraint_func),
        (('Nurpia', 'Nesa'), constraint_func),

        (('Istajib', 'Sigit'), constraint_func),
        (('Istajib', 'Ghina'), constraint_func),

        (('Sigit', 'Najwa'), constraint_func),
        (('Sigit', 'Nesa'), constraint_func),

        (('Ilmi', 'Nesa'), constraint_func),

        (('Najwa', 'Nesa'), constraint_func)
    ]

    problem = CspProblem(
        names,
        colors,
        constraints
    )

    output = backtrack(problem)

    print("\nColor Mapping:\n")

    for k, v in output.items():
        print(k, "=>", v)
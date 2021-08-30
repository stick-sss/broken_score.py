from prac_06.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(f"{ruby}\n{python}\n{visual_basic}")
    programminglanguage_list = [ruby, python, visual_basic]
    for programlanguage in programminglanguage_list:
        if programlanguage.is_dynamic():
            print(programlanguage.name)
main()
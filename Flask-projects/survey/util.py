from . import app

tables=['Regions', 'Districts', 'Buildings', 'Schools', 'Respondents', 'Sections', 'Questions', 'Answers']

if __name__ == "__main__":
    app.drop_all_tables(tables)

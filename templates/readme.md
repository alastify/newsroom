# Šablony
V tomto adresáři lze přetěžovat šablony z dílčích aplikací.

## Postup
Jednoduše zkopírujte obsah adresáře ``templates`` z dané aplikace sem.

Např. app ``newsroom`` obsahuje podadresář ``templates``, ve kterém se nachází další podadresář ``newsroom``

    newsroom
        | - templates
        |    |- newsroom
        |    |      base.html
        |    |      index.html
        |    |      ...
    templates


Zkopírujte tedy tento vnořený ``newsroom`` tak, aby se nacházel v tomto adresáři. Výsledek tedy bude:

    newsroom
        | - templates
        |    |- newsroom
        |    |      base.html
        |    |      index.html
        |    |      ...
    templates
        |- newsroom
        |      base.html
        |      index.html
        |      ...

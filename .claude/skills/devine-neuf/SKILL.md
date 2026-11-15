---
name: devine-neuf
description: Publish or add questions for Devine Neuf, a personal movie and TV party game. Read the questions marked "Validée" in the Notion bank, check them, show them to the owner, and push them to the game only after the owner approves. Also drafts new questions on request. Use on "publie le jeu", "ajoute une question", "nouvelles questions", "propose des questions sur X", or any request about the Devine Neuf question bank.
metadata:
  version: "2.0"
---

# devine-neuf

Personal project. The answers to the owner are in French. Run it on the owner's Mac (directly or through Remote Control),
because only the Mac has the GitHub access. Do not use a cloud session.

| Item | Value |
|---|---|
| Game file | `~/perso/devine-neuf/index.html` (the `BANK` array) |
| Repo | https://github.com/AlexLA92/devine-neuf (push to `main`) |
| Live site | https://alexla92.github.io/devine-neuf/ (rebuilds in about 1 min) |
| Notion bank | https://app.notion.com/p/f6e729d442d1448c8819df7c3c9920f9, data source `collection://e9c98dc0-2600-4424-95b7-221cc9aa9afd` |
| Check script | `python3 ~/perso/devine-neuf/.claude/skills/devine-neuf/check.py` |

## Rules for a question

- Exactly 9 answers. One category: Films, Séries, Personnages, Sagas, Acteurs, Récompenses. One difficulty: Facile, Moyen, Difficile.
- A list can be open (decision of 2026-11-15): "9 films de Scorsese" is fine. A right answer that is not in the grid
  does not count. Do not flag an open list as a problem.
- A list must not be wrong. Flag a title that does not match its answers, for example "après 2010" with a 2010 film,
  or "les 9 films de X" when X made 10. Propose a corrected title.

## Rule: the owner approves before the push

Never edit `index.html`, never write to Notion, never commit or push before the owner approves in the chat.
"Validée" in Notion is the owner's choice of questions. The owner still sees the check results before the push.

## Flow A: "publie le jeu" (the owner added questions in Notion)

1. Run the check script to list the questions in the game.
2. Query the Notion data source for rows with `Statut` = `Validée`. Keep the rows whose question is not in the game.
   Also list the questions in the game whose Notion row is now `Rejetée`: these must leave the game.
3. Check each new question: 9 answers, category, difficulty, facts. Use web search for any list you are not sure of,
   and always for events after 2023.
4. Show one table: question, verdict (OK / title to fix / error), detail. Then ask "Je publie ?" and wait.
5. After approval: go to "Publish" below.

## Flow B: "propose des questions sur X"

1. Run the check script, so you do not make a duplicate.
2. Draft the questions. Favor series and characters, because the target player watches more series than films.
3. Check the facts as in flow A.
4. Show one table per question (number, answer, other spellings), with the category and the difficulty. Ask
   "Je les ajoute ? Dis-moi lesquelles garder ou corriger." and wait. Keep tables narrow, because the owner often reads on a phone.
5. After approval: create the Notion rows (`Statut` = `Validée`), then go to "Publish".

## Publish

1. Add one line per question at the end of `BANK` in `index.html`:
   `{q:"…",c:"Séries",d:"Moyen",a:"Réponse 1|Other spelling|Other spelling ; Réponse 2 ; … (9 answers)"},`
   Turn the Notion column `Variantes acceptées` into "|" spellings on the matching answer. Add the obvious ones
   that are missing (English title, surname alone).
2. Remove the lines of questions that are now `Rejetée` in Notion.
3. Run the check script. Fix any error before you continue.
4. Apply the approved title fixes in Notion too, so Notion and the game show the same text.
5. In `~/perso/devine-neuf`: commit with a message like `Ajoute 3 questions : Scorsese, Lynch, De Niro`, then `git push`.
   The repo git config already uses the GitHub noreply email. Do not change it.
6. Wait about 1 minute, then check that the live site contains one new question text (curl and grep).
7. Report in 3 lines: questions added or removed, new total, live link.

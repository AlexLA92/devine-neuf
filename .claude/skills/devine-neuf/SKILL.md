---
name: devine-neuf
description: Add questions to Devine Neuf, a personal movie and TV party game. Draft each question with exactly 9 answers, check the facts, show them to the owner, and add them to the game only after the owner approves. Use on "ajoute une question", "nouvelles questions", "enrichis la banque", "propose des questions sur X", "publie le jeu", or any request about the Devine Neuf question bank.
metadata:
  version: "1.1"
---

# devine-neuf

Personal project. The answers to the owner are in French.

| Item | Value |
|---|---|
| Game file | `index.html` at the repo root (the `BANK` array) |
| Repo | https://github.com/AlexLA92/devine-neuf |
| Live site | https://alexla92.github.io/devine-neuf/ (rebuilds from `main` in about 1 min) |
| Notion bank | https://app.notion.com/p/f6e729d442d1448c8819df7c3c9920f9, data source `collection://e9c98dc0-2600-4424-95b7-221cc9aa9afd` |
| Check script | `python3 .claude/skills/devine-neuf/check.py` (run from the repo root) |

## Rule: the owner approves before anything is written

Never edit `index.html`, never write to Notion, never commit or push before the owner approves the questions in the chat.
"Ajoute" or "publie" in the first request is not an approval of questions the owner has not seen.

## Two modes

| Mode | How to know | Publish step |
|---|---|---|
| Local | The repo is at `~/perso/devine-neuf` on a Mac | Commit on `main` and push. The site updates. |
| Web | Any other place (a Claude Code cloud session, often opened from a phone) | Commit on a new branch, push it, open a pull request. The site updates when the owner merges the PR. |

## Steps

1. **Read the bank.** Run the check script. It prints the questions that exist, so you do not make a duplicate.
2. **Draft.** For each question:
   - Exactly 9 answers. A closed list that a player can check (a filmography, a cast, a list of awards by year).
   - Add the limit that makes the list closed, for example "jusqu'à 2014" or "cérémonies 2016 à 2024".
   - Add the other spellings a player can say: the English title, a short name, a surname alone.
   - A category from: Films, Séries, Personnages, Sagas, Acteurs, Récompenses. A difficulty from: Facile, Moyen, Difficile.
   - Favor series and characters, because the target player watches more series than films.
3. **Check the facts.** Use web search for every list that you do not know with certainty, and always for events after 2023.
   Say which questions you checked on the web.
4. **Show the draft and stop.** One table per question: number, answer, other spellings. Under each table, give
   the category, the difficulty and one line on how you checked it. End with:
   "Je les ajoute ? Dis-moi lesquelles garder ou corriger." Then wait. On a phone, keep the tables narrow (3 columns).
5. **After approval only**, for the approved questions:
   1. Add one line per question at the end of `BANK` in `index.html`, in this format:
      `{q:"…",c:"Séries",d:"Moyen",a:"Réponse 1|Other spelling ; Réponse 2 ; … (9 answers)"},`
   2. Run the check script. Fix any error before you continue.
   3. If the Notion tools are available, create one Notion row per question in the data source above: `Question`,
      `Catégorie`, `Difficulté`, `Statut` = `Validée`, `Réponses` = the 9 main answers separated by " ; ",
      `Variantes acceptées` = the other spellings. If the Notion tools are not available, skip this step and say so.
   4. Commit with a message like `Ajoute 2 questions : Spielberg, Friends`, then publish as the mode table says.
      In local mode, the repo git config already uses the GitHub noreply email. Do not change it.
   5. Local mode: wait about 1 minute, then check that the live site contains the new question text (curl and grep).
      Web mode: give the PR link and say "Fusionne la PR pour mettre le site à jour."
6. **Report** in 3 lines: questions added, new total, then the live link (local) or the PR link (web).

## Rejected questions

A question that the owner rejects must not be in `BANK`. Remove its line, set the Notion `Statut` to `Rejetée` when Notion
is available, run the check script, and publish, after the same approval.

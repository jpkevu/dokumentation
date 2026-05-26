import streamlit as st

# Titel
st.title("Dokumentation af fremskrivningsmodel for elektrikeruddannelsen")

# Formål
st.header("Formål")
st.write("""
Formålet med modellen er at fremskrive tilgang, frafald og bestand på elektrikeruddannelsen frem til 2036, 
baseret på historiske data, befolkningsfremskrivninger og en række metodiske antagelser.

Derudover indgår flere scenarier, der tager højde for den forventede indførelse af EPX (Erhvervsparat X) fra 2030, 
hvor andelen af elever, der vælger EPX, varierer (20%, 30%, 40%, 50%). Dette påvirker fordelingen af aldersgrupper blandt nye GF2-elever.
""")

# Datagrundlag
st.header("Datagrundlag")
st.write("""
- **Befolkningstal (FOLK2_filtered.xlsx):** Befolkning fordelt på aldersgrupper. Fremskrivningsdata fra Danmarks Statistik.
- **Tilgang til GF2 elektriker (Tilgang_GF2_elektriker.xlsx):** Antal elever, der starter på GF2 elektrikeruddannelsen.
- **Tilgang til GF2 samlet (Tilgang_GF2.xlsx):** Samlet antal GF2-elever.
- **Bestand elektriker (bestand_elektriker.xlsx):** Historisk bestand af elever på elektrikeruddannelsen.
- **Bestand total (bestand_total.xlsx):** Samlet bestand af GF2-elever.
- **Frafaldsandele elektriker (frafald_andele.xlsx):** Historiske frafaldsandele på elektrikeruddannelsen.
Dækning: 2016-2024 (Befolkningstal 2016-2036)
Aldersgrupper: 15-17 år, 18-19 år, 20-24 år, 25+ år
""")

# Metoder
st.header("Metoder")
st.subheader("1. Tilgang til GF2 elektriker")
st.write("""
- Historiske andele er beregnet ift. både den samlede GF2-tilgang og befolkningen i aldersgrupperne.
- For begge mål er estimeret en lineær trend (mindste kvadraters metode).
- Fremskrivning (2025-2036) beregnes som vægtet gennemsnit af de to trends, multipliceret med hhv. fremskrevet GF2-tilgang og befolkningstal.
""")

st.subheader("2. Frafaldsandele")
st.write("""
- Frafald er ikke modelleret separat i fremskrivningen.
- Der anvendes i stedet en fast antagelse om, at 37% af en elevkohorte falder fra i løbet af uddannelsesforløbet baseret på DEAs analyse af vvs-energi og elektrikeruddannelserne.
- Det betyder, at 63% af en tilgangsårgang indgår i den fremtidige bestand.
""")

st.subheader("3. Bestand af elektriker-elever")
st.write("""
- Bestanden af elektriker-elever beregnes ud fra tidligere års tilgang til uddannelsen.
- Hver tilgangsårgang følges over tid i en 4-årig kohortemodel.
- Der anvendes en fast antagelse om, at 37% falder fra i løbet af uddannelsesforløbet.
- Bestanden i et givent år er summen af de seneste års tilgange, fordelt på aldersgrupper og reduceret for frafald.
""")

# EPX-scenarier
st.header("EPX-scenarier (fra 2030)")
st.write("""
Fra 2030 indføres EPX, hvilket ændrer fordelingen af elever på GF2. Flere scenarier baseret på hvor mange procent af årgangen, der vælger EPX:
- Uden EPX
- 20% EPX
- 30% EPX
- 40% EPX
- 50% EPX

Antagelser:
- Hvis få vælger EPX, starter flere direkte på GF2. Hvis mange vælger EPX, reduceres den direkte GF2-tilgang tilsvarende.
- EPX varer to år, hvilket betyder, at størstedelen af eleverne først fremgår som tilgang på GF2 i 18-19-årsgruppen.
- Effekten er gradvis, hvor faldet i 15-17-årige først for alvor ses fra 2031.
- Ca. 60% af EPX-eleverne antages at vælge erhvervsuddannelse. Andelen af elektrikere beregnes ud fra historiske data.
""")

# Antagelser og forbehold
st.header("Antagelser og forbehold")
st.write("""
1. Lineær udvikling: Tilgang og bestand antager lineære trends i andele; faktiske ændringer kan være ikke-lineære eller påvirket af reformer.
2. Glidende gennemsnit: Frafaldet modelleres med glidende gennemsnit, som stabiliserer data men ikke fanger trends.
3. Fremskrivning af totalbestand og befolkning: Manglende værdier erstattes med historiske gennemsnit.
4. EPX-implementering: Antagelsen om procentandel af årgangen på EPX er et skøn.
5. Ingen usikkerhedsintervaller: Fremskrivningen er deterministisk.
""")

# Output
st.header("Output")
st.write("""
Resultatet er gjort tilgængeligt i et interaktivt PowerBI-dashboard, hvor brugeren kan:
- Vælge mellem scenarier (Uden EPX, 20%, 30%, 40%, 50% EPX)
- Analysere forskellige aldersgrupper og parametre (tilgang, frafald, bestand)
- Se effekten af EPX på aldersfordeling og samlet elektrikerbestand
""")

# PDF download fra lokal fil
pdf_path = "Dokumentation til fremskrivning.pdf"  # Filen skal ligge i samme mappe som appen

with open(pdf_path, "rb") as pdf_file:
    PDF = pdf_file.read()

st.download_button(
    label="Hent PDF-dokumentation",
    data=PDF,
    file_name="Dokumentation til fremskrivning.pdf",
    mime="application/pdf"
)

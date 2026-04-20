# Properties near the sea search guide

**Session ID:** ses_25428567effe65nkGqdM06q9Ig
**Created:** 4/20/2026, 7:02:10 PM
**Updated:** 4/20/2026, 7:02:23 PM

---

## User

find  me properties close to the sea

---

## Assistant (Build · Big Pickle · 7.2s)

_Thinking:_

The user is asking about properties close to the sea. This is a wiki about summer holidays in Italy, so they want to find vacation properties near the sea/beach. Let me query the knowledge base to find relevant properties.


**Tool: qmd_query**

**Input:**
```json
{
  "searches": [
    {
      "type": "lex",
      "query": "sea beach close proximity"
    },
    {
      "type": "vec",
      "query": "properties near the sea beach access"
    }
  ]
}
```

**Output:**
```
Found 10 results for "sea beach close proximity":

#36f781 88% wiki/private-beach.md - Private Beach Access
#c05f23 52% wiki/beach-access.md - Beach Access
#e7dccd 38% wiki/townhouse-scalea.md - Townhouse Scalea
#4d3fff 35% wiki/home-pollica.md - Home Pollica
#e938e3 34% wiki/home-rio-claro.md - Home Rio Claro
#19702d 34% wiki/townhouse-castellaneta.md - Townhouse Castellaneta Marina
#9bfc7b 34% wiki/cilento-coast.md - Cilento Coast
#2f77f8 33% wiki/home-scario.md - Home Scario
#43c6bf 33% wiki/home-villapiana-lido.md - Home Villapiana Lido
#35d545 33% wiki/cottage-marina-camerota.md - Cottage Marina di Camerota
```

---

## Assistant (Build · Big Pickle · 1.4s)

_Thinking:_

Got search results for properties close to the sea. Let me fetch some of the top results to provide more details.




Found several properties close to the sea. Let me get the details:


**Tool: qmd_get**

**Input:**
```json
{
  "file": "wiki/private-beach.md",
  "maxLines": 50
}
```

**Output:**
```
# Private Beach Access

**Summary**: Properties with private or exclusive beach access.

**Last updated**: 2026-04-19

---

## Properties with Private Beach Access

### True Private Access

| Property | Location | Notes |
|----------|----------|-------|
| [[home-pollica]] | Pollica, Cilento | Private access road, limited users |
| [[townhouse-scalea]] | Scalea | From complex, 100m |

### Shared but Exclusive

| Property | Location | Notes |
|----------|----------|-------|
| [[home-fondi-emanuele]] | Fondi | Beachfront (120m) |
| [[home-palinuro]] | Palinuro | Beachfront (200m) |
| [[home-pisciotta]] | Pisciotta | Walkable to marina |

## Note on "Private"

Many listings claim "private" beach access when they mean:
- Reserved for residence guests only
- Not a public beach
- Limited number of users

True private access is rare - [[home-pollica]] and [[townhouse-scalea]] are the best options.

## Related pages

- [[home-pollica]]
- [[townhouse-scalea]]
- [[calabria-coast]]
- [[cilento-coast]]
```

**Tool: qmd_get**

**Input:**
```json
{
  "file": "wiki/beach-access.md",
  "maxLines": 50
}
```

**Output:**
```
# Beach Access

**Summary**: Summary of beach distances across all properties.

**Last updated**: 2026-04-19

---

## By Distance

### Closest (Beachfront/Private)

- [[home-pollica]] - Private (300m)
- [[home-palinuro]] - Beachfront (200m)
- [[home-fondi-emanuele]] - Beachfront (120m)
- [[home-pisciotta]] - Walkable
- [[home-gaeta-luca]] - 300m

### Walking Distance (200-600m)

- [[home-fondi-luisa]] - 50m
- [[home-villapiana-lido]] - 200m
- [[villa-castellaneta]] - Walkable
- [[townhouse-castellaneta]] - 200m (5 min)
- [[home-rio-claro]] - 600m

### Drive Required

- [[villa-san-felice-circeo]] - Walkable/bike
- [[villa-fondi-serena]] - 800m (15 min walk)
- [[townhouse-scalea]] - 100m
- [[villa-hotel-tivigest]] - 500m

## Related pages

- [[private-beach]]
- [[lazio-coast]]
- [[calabria-coast]]
```

---

## Assistant (Build · Big Pickle · 3.3s)

_Thinking:_

Great, I now have good information about properties close to the sea. Let me summarize this for the user in a useful way.




Here are properties sorted by proximity to the sea:

## Beachfront (walking distance)
- **[[home-pollica]]** - Private access (300m) - Pollica, Cilento
- **[[home-palinuro]]** - Beachfront (200m) - Palinuro
- **[[home-fondi-emanuele]]** - Beachfront (120m) - Fondi
- **[[home-pisciotta]]** - Walkable to marina - Pisciotta

## Very Close (under 5 min walk)
- **[[home-fondi-luisa]]** - 50m - Fondi
- **[[home-villapiana-lido]]** - 200m - Villapiana Lido
- **[[townhouse-castellaneta]]** - 200m (5 min) - Castellaneta Marina
- **[[townhouse-scalea]]** - 100m - Scalea

## Walking Distance (5-10 min)
- **[[home-rio-claro]]** - 600m - Rio Claro
- **[[villa-fondi-serena]]** - 800m (15 min walk) - Fondi

## Best Options with Private Access
Only a few have **true private** beach access:
- **[[home-pollica]]** - Private access road, limited users
- **[[townhouse-scalea]]** - 100m from complex

Want me to get details on any specific property?

---


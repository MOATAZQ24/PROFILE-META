## Technical Philosophy

> "Building scalable solutions with Python/ML focus"

## Skills Radar

```r
library(plotly)
skills <- data.frame(
  skill = c("Python", "ML", "Docker", "SQL", "React"),
  level = c(9, 8, 6, 7, 5)
)

plot_ly(skills, r = ~level, theta = ~skill, fill = "toself") %>%
  add_trace(mode = "lines", line = list(color = "darkblue")) %>%
  layout(
    polar = list(
      radialaxis = list(
        visible = T,
        range = c(0,10)
      )
    ),
    showlegend = F
  )
```

## Contribution Heatmap Overlay

(This section will be dynamically updated by GitHub Actions.)


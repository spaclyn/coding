# Load required libraries
library(ggplot2)
library(dplyr)
library(tidyr)
library(stringr)

# Read the dataset
setwd("\\Users\\aj\\Desktop\\coding\\r\\lotr analysis")

lotr <- read.csv("lotr_characters.csv",
                 stringsAsFactors = FALSE, na.strings = c("", "NA"))


cat("LOTR CHARACTERS DATASET ANALYSIS\n")
cat("========================================\n\n")

# Display basic dataset information
cat("Dataset Dimensions:\n")
cat("Number of characters:", nrow(lotr), "\n")
cat("Number of attributes:", ncol(lotr), "\n\n")

cat("Column Names:\n")
print(names(lotr))
cat("\n")

cat("First few rows:\n")
print(head(lotr, 3))
cat("\n\n")



cat("OPERATION 1: MISSING VALUES ANALYSIS\n")
cat("========================================\n")

missing_counts <- colSums(is.na(lotr))
missing_percentages <- round((missing_counts / nrow(lotr)) * 100, 2)
missing_df <- data.frame(
  Column = names(lotr),
  Missing_Count = missing_counts,
  Missing_Percentage = missing_percentages
)

print(missing_df)

# Explicitly print and save the plot
p1 <- ggplot(missing_df, aes(x=reorder(Column, -Missing_Percentage), y=Missing_Percentage)) +
  geom_bar(stat="identity", fill="steelblue") +
  geom_text(aes(label=paste0(Missing_Percentage, "%")), vjust=-0.5, size=3.5) +
  labs(title="Missing Data Analysis by Attribute",
       x="Attribute", y="Percentage Missing (%)") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle=45, hjust=1))

# Save using ggsave
ggsave("missingData.png", plot = p1, width = 8, height = 6, dpi = 100)
print(p1)

cat("\nVisualization saved as: missingData.png\n\n")



cat("OPERATION 2: RACE DISTRIBUTION\n")
cat("========================================\n")

race_dist <- lotr %>%
  filter(!is.na(race)) %>%
  group_by(race) %>%
  summarise(Count = n()) %>%
  arrange(desc(Count))

print(race_dist)

cat("\nTotal characters with race information:", sum(race_dist$Count), "\n")

# Visualize race distribution
p2 <- ggplot(race_dist, aes(x=reorder(race, -Count), y=Count, fill=race)) +
  geom_bar(stat="identity") +
  geom_text(aes(label=Count), vjust=-0.5) +
  labs(title="Character Distribution by Race",
       x="Race", y="Number of Characters") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle=45, hjust=1),
        legend.position = "none")

ggsave("raceDistribution.png", plot = p2, width = 8, height = 6, dpi = 100)
print(p2)
cat("Visualization saved as: raceDistribution.png\n\n")



cat("OPERATION 3: GENDER DISTRIBUTION BY RACE\n")
cat("========================================\n")

gender_race <- lotr %>%
  filter(!is.na(gender) & !is.na(race)) %>%
  group_by(race, gender) %>%
  summarise(Count = n(), .groups = 'drop') %>%
  arrange(race, desc(Count))

print(gender_race)

# Calculate gender ratio for each race
gender_ratio <- lotr %>%
  filter(!is.na(gender) & !is.na(race)) %>%
  group_by(race) %>%
  summarise(
    Total = n(),
    Male = sum(gender == "Male", na.rm=TRUE),
    Female = sum(gender == "Female", na.rm=TRUE),
    Male_Percentage = round((Male/Total)*100, 1),
    Female_Percentage = round((Female/Total)*100, 1)
  ) %>%
  arrange(desc(Total))

cat("\nGender Ratios by Race:\n")
print(gender_ratio)

# Visualize
p3 <- ggplot(gender_race, aes(x=race, y=Count, fill=gender)) +
  geom_bar(stat="identity", position="dodge") +
  labs(title="Gender Distribution Across Races",
       x="Race", y="Count", fill="Gender") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle=45, hjust=1))

ggsave("graceRace.png", plot = p3, width = 9, height = 6, dpi = 100)
print(p3)
cat("Visualization saved as: graceRace.png\n\n")



cat("OPERATION 4: HEIGHT ANALYSIS\n")
cat("========================================\n")

# Extract numeric height values (convert various formats to cm)
lotr$height_numeric <- sapply(lotr$height, function(h) {
  if(is.na(h)) return(NA)
  
  # Extract feet and inches
  if(grepl("'", h)) {
    # Extract the feet'inches format
    matches <- str_extract(h, "\\d+['']\\d*")
    if(!is.na(matches)) {
      parts <- str_split(matches, "'")[[1]]
      feet <- as.numeric(parts[1])
      inches <- ifelse(length(parts) > 1, as.numeric(gsub("\"", "", parts[2])), 0)
      return(feet * 30.48 + inches * 2.54)  # Convert to cm
    }
  }
  
  # Extract meters
  if(grepl("m", tolower(h))) {
    meters <- as.numeric(str_extract(h, "\\d+\\.\\d+"))
    if(!is.na(meters)) return(meters * 100)
  }
  
  return(NA)
})

height_stats <- lotr %>%
  filter(!is.na(height_numeric) & !is.na(race)) %>%
  group_by(race) %>%
  summarise(
    Count = n(),
    Mean_Height_cm = round(mean(height_numeric, na.rm=TRUE), 2),
    Median_Height_cm = round(median(height_numeric, na.rm=TRUE), 2),
    Min_Height_cm = round(min(height_numeric, na.rm=TRUE), 2),
    Max_Height_cm = round(max(height_numeric, na.rm=TRUE), 2),
    SD_Height_cm = round(sd(height_numeric, na.rm=TRUE), 2)
  ) %>%
  arrange(desc(Mean_Height_cm))

cat("Height Statistics by Race (in centimeters):\n")
print(height_stats)

# Overall height statistics
overall_height <- lotr %>%
  filter(!is.na(height_numeric)) %>%
  summarise(
    Count = n(),
    Mean = round(mean(height_numeric), 2),
    Median = round(median(height_numeric), 2),
    SD = round(sd(height_numeric), 2),
    Min = round(min(height_numeric), 2),
    Max = round(max(height_numeric), 2)
  )

cat("\nOverall Height Statistics:\n")
print(overall_height)

# Visualize
p4 <- lotr %>%
  filter(!is.na(height_numeric) & !is.na(race)) %>%
  ggplot(aes(x=race, y=height_numeric, fill=race)) +
  geom_boxplot() +
  labs(title="Height Distribution by Race",
       x="Race", y="Height (cm)") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle=45, hjust=1),
        legend.position = "none")

ggsave("heightRace.png", plot = p4, width = 8, height = 6, dpi = 100)
print(p4)
cat("Visualization saved as: heightRace.png\n\n")


cat("OPERATION 5: MARITAL STATUS ANALYSIS\n")
cat("========================================\n")

# Categorize marital status
lotr$marital_status <- sapply(lotr$spouse, function(s) {
  if(is.na(s)) return("Unknown")
  s_lower <- tolower(s)
  if(grepl("none|never married|unmarried|not married", s_lower)) return("Single")
  if(grepl("unnamed wife|unnamed husband|wife|husband", s_lower)) return("Married")
  if(grepl("loved", s_lower)) return("Unmarried (In Love)")
  return("Married")
})

marital_summary <- lotr %>%
  filter(!is.na(race)) %>%
  group_by(race, marital_status) %>%
  summarise(Count = n(), .groups = 'drop') %>%
  arrange(race, desc(Count))

print(marital_summary)

# Overall marital status
overall_marital <- table(lotr$marital_status)
cat("\nOverall Marital Status Distribution:\n")
print(overall_marital)

# Visualize
p5 <- ggplot(marital_summary, aes(x=race, y=Count, fill=marital_status)) +
  geom_bar(stat="identity", position="fill") +
  scale_y_continuous(labels = scales::percent) +
  labs(title="Marital Status Distribution by Race (Proportional)",
       x="Race", y="Percentage", fill="Marital Status") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle=45, hjust=1))

ggsave("maritalStatus.png", plot = p5, width = 9, height = 6, dpi = 100)
print(p5)
cat("Visualization saved as: maritalStatus.png\n\n")



cat("OPERATION 6: HAIR COLOR DISTRIBUTION\n")
cat("========================================\n")

# Simplify hair color categories
lotr$hair_simple <- sapply(lotr$hair, function(h) {
  if(is.na(h)) return(NA)
  h_lower <- tolower(h)
  if(grepl("golden|gold|blonde|yellow", h_lower)) return("Golden/Blonde")
  if(grepl("dark|black|brown", h_lower)) return("Dark/Brown")
  if(grepl("red|auburn", h_lower)) return("Red")
  if(grepl("silver|white|grey|gray", h_lower)) return("Silver/White/Grey")
  if(grepl("none", h_lower)) return("None")
  return("Other")
})

hair_dist <- lotr %>%
  filter(!is.na(hair_simple) & !is.na(race)) %>%
  group_by(race, hair_simple) %>%
  summarise(Count = n(), .groups = 'drop') %>%
  arrange(race, desc(Count))

print(hair_dist)

# Top hair colors overall
top_hair <- lotr %>%
  filter(!is.na(hair_simple)) %>%
  group_by(hair_simple) %>%
  summarise(Count = n()) %>%
  arrange(desc(Count))

cat("\nMost Common Hair Colors:\n")
print(top_hair)

# Visualize
p6 <- lotr %>%
  filter(!is.na(hair_simple) & !is.na(race)) %>%
  ggplot(aes(x=race, fill=hair_simple)) +
  geom_bar(position="fill") +
  scale_y_continuous(labels = scales::percent) +
  labs(title="Hair Color Distribution by Race (Proportional)",
       x="Race", y="Percentage", fill="Hair Color") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle=45, hjust=1))

ggsave("hairColor.png", plot = p6, width = 9, height = 6, dpi = 100)
print(p6)
cat("Visualization saved as: hairColor.png\n\n")



cat("OPERATION 7: AGE AND LIFESPAN ANALYSIS\n")
cat("========================================\n")

# Function to extract year from complex date strings
extract_year <- function(date_str) {
  if(is.na(date_str)) return(NA)
  
  # Look for patterns
  age_match <- str_extract(date_str, "(TA|SA|FA|FO|SR|YT)\\s*\\d+")
  if(!is.na(age_match)) {
    parts <- str_split(age_match, "\\s+")[[1]]
    age <- parts[1]
    year <- as.numeric(parts[2])
    
    # Normalize to a common timeline (rough approximation)
    if(age == "FA") return(year)
    if(age == "SA") return(3000 + year)
    if(age == "TA") return(6000 + year)
    if(age == "FO" || age == "SR") return(9000 + year)
    return(year)
  }
  
  # Look for just numbers
  num_match <- as.numeric(str_extract(date_str, "\\d+"))
  if(!is.na(num_match)) return(num_match)
  
  return(NA)
}

# Calculate ages
lotr$birth_year <- sapply(lotr$birth, extract_year)
lotr$death_year <- sapply(lotr$death, extract_year)

lotr$lifespan <- ifelse(!is.na(lotr$birth_year) & !is.na(lotr$death_year),
                        lotr$death_year - lotr$birth_year,
                        NA)

# Characters with known lifespans
lifespan_data <- lotr %>%
  filter(!is.na(lifespan) & lifespan > 0 & lifespan < 10000 & !is.na(race)) %>%
  group_by(race) %>%
  summarise(
    Count = n(),
    Mean_Lifespan = round(mean(lifespan, na.rm=TRUE), 1),
    Median_Lifespan = round(median(lifespan, na.rm=TRUE), 1),
    Min_Lifespan = round(min(lifespan, na.rm=TRUE), 1),
    Max_Lifespan = round(max(lifespan, na.rm=TRUE), 1),
    SD_Lifespan = round(sd(lifespan, na.rm=TRUE), 1)
  ) %>%
  arrange(desc(Mean_Lifespan))

cat("Lifespan Statistics by Race (in years):\n")
print(lifespan_data)

# Find longest-lived characters
longest_lived <- lotr %>%
  filter(!is.na(lifespan) & lifespan > 0) %>%
  select(name, race, lifespan) %>%
  arrange(desc(lifespan)) %>%
  head(10)

cat("\nTop 10 Longest-Lived Characters:\n")
print(longest_lived)

# Visualize
p7 <- lotr %>%
  filter(!is.na(lifespan) & lifespan > 0 & lifespan < 5000 & !is.na(race)) %>%
  ggplot(aes(x=race, y=lifespan, fill=race)) +
  geom_boxplot() +
  labs(title="Lifespan Distribution by Race (excluding immortals)",
       x="Race", y="Lifespan (years)") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle=45, hjust=1),
        legend.position = "none")

ggsave("lifespan.png", plot = p7, width = 8, height = 6, dpi = 100)
print(p7)
cat("Visualization saved as: lifespan.png\n\n")



cat("OPERATION 8: REALM/KINGDOM DISTRIBUTION\n")
cat("========================================\n")

# Extract primary realm (first one listed)
lotr$primary_realm <- sapply(lotr$realm, function(r) {
  if(is.na(r)) return(NA)
  # Take first realm if multiple are listed
  first_realm <- str_trim(str_split(r, ",")[[1]][1])
  return(first_realm)
})

realm_dist <- lotr %>%
  filter(!is.na(primary_realm)) %>%
  group_by(primary_realm) %>%
  summarise(Count = n()) %>%
  arrange(desc(Count)) %>%
  head(15)  # Top 15 realms

cat("Top 15 Most Populated Realms:\n")
print(realm_dist)

# Realm by race
realm_race <- lotr %>%
  filter(!is.na(primary_realm) & !is.na(race)) %>%
  group_by(primary_realm, race) %>%
  summarise(Count = n(), .groups = 'drop') %>%
  arrange(primary_realm, desc(Count))

cat("\nRealm Distribution by Race (sample):\n")
print(head(realm_race, 20))

# Visualize
p8 <- ggplot(realm_dist, aes(x=reorder(primary_realm, Count), y=Count)) +
  geom_bar(stat="identity", fill="darkgreen") +
  geom_text(aes(label=Count), hjust=-0.2, size=3) +
  coord_flip() +
  labs(title="Top 15 Most Populated Realms/Kingdoms",
       x="Realm", y="Number of Characters") +
  theme_minimal()

ggsave("realms.png", plot = p8, width = 9, height = 7, dpi = 100)
print(p8)
cat("Visualization saved as: realms.png\n\n")


cat("OPERATION 9: NAME PATTERN ANALYSIS\n")
cat("========================================\n")

# Calculate name lengths
lotr$name_length <- nchar(lotr$name)

name_stats <- lotr %>%
  filter(!is.na(name) & !is.na(race)) %>%
  group_by(race) %>%
  summarise(
    Count = n(),
    Mean_Name_Length = round(mean(name_length, na.rm=TRUE), 2),
    Median_Name_Length = median(name_length, na.rm=TRUE),
    Min_Name_Length = min(name_length, na.rm=TRUE),
    Max_Name_Length = max(name_length, na.rm=TRUE)
  ) %>%
  arrange(desc(Mean_Name_Length))

cat("Name Length Statistics by Race:\n")
print(name_stats)

# Longest and shortest names
longest_names <- lotr %>%
  filter(!is.na(name)) %>%
  arrange(desc(name_length)) %>%
  select(name, race, name_length) %>%
  head(10)

cat("\nTop 10 Longest Character Names:\n")
print(longest_names)

shortest_names <- lotr %>%
  filter(!is.na(name) & name_length > 0) %>%
  arrange(name_length) %>%
  select(name, race, name_length) %>%
  head(10)

cat("\nTop 10 Shortest Character Names:\n")
print(shortest_names)

# Visualize
p9 <- lotr %>%
  filter(!is.na(name_length) & !is.na(race)) %>%
  ggplot(aes(x=race, y=name_length, fill=race)) +
  geom_violin(alpha=0.7) +
  geom_boxplot(width=0.2, alpha=0.5) +
  labs(title="Name Length Distribution by Race",
       x="Race", y="Number of Characters in Name") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle=45, hjust=1),
        legend.position = "none")

ggsave("nameLength.png", plot = p9, width = 8, height = 6, dpi = 100)
print(p9)
cat("Visualization saved as: nameLength.png\n\n")



cat("OPERATION 10: DATA COMPLETENESS ANALYSIS\n")
cat("========================================\n")

# Calculate completeness score for each character
lotr$completeness_score <- rowSums(!is.na(lotr[, c("birth", "death", "gender", 
                                                     "hair", "height", "race", 
                                                     "realm", "spouse")])) / 8 * 100

completeness_by_race <- lotr %>%
  filter(!is.na(race)) %>%
  group_by(race) %>%
  summarise(
    Count = n(),
    Mean_Completeness = round(mean(completeness_score, na.rm=TRUE), 2),
    Median_Completeness = round(median(completeness_score, na.rm=TRUE), 2),
    Min_Completeness = round(min(completeness_score, na.rm=TRUE), 2),
    Max_Completeness = round(max(completeness_score, na.rm=TRUE), 2)
  ) %>%
  arrange(desc(Mean_Completeness))

cat("Data Completeness Score by Race (%):\n")
print(completeness_by_race)

# Most complete character profiles
most_complete <- lotr %>%
  select(name, race, completeness_score) %>%
  arrange(desc(completeness_score)) %>%
  head(15)

cat("\nTop 15 Most Complete Character Profiles:\n")
print(most_complete)

# Least complete (excluding 0% which are likely data entry errors)
least_complete <- lotr %>%
  filter(completeness_score > 0) %>%
  select(name, race, completeness_score) %>%
  arrange(completeness_score) %>%
  head(10)

cat("\nTop 10 Least Complete Character Profiles:\n")
print(least_complete)

# Visualize
p10 <- ggplot(lotr, aes(x=completeness_score)) +
  geom_histogram(binwidth=12.5, fill="coral", color="black", alpha=0.7) +
  geom_vline(aes(xintercept=mean(completeness_score, na.rm=TRUE)), 
             color="red", linetype="dashed", size=1) +
  labs(title="Distribution of Character Profile Completeness",
       subtitle=paste("Red line indicates mean completeness (", 
                      round(mean(lotr$completeness_score, na.rm=TRUE), 1), "%)", sep=""),
       x="Completeness Score (%)", y="Number of Characters") +
  theme_minimal()

ggsave("completeness.png", plot = p10, width = 8, height = 6, dpi = 100)
print(p10)
cat("Visualization saved as: completeness.png\n\n")


# SUMMARY STATISTICS
# ============================================================================
cat("FINAL SUMMARY\n")
cat("========================================\n")

cat("\nDataset Overview:\n")
cat("- Total Characters:", nrow(lotr), "\n")
cat("- Characters with Race Info:", sum(!is.na(lotr$race)), "\n")
cat("- Characters with Gender Info:", sum(!is.na(lotr$gender)), "\n")
cat("- Characters with Height Info:", sum(!is.na(lotr$height_numeric)), "\n")
cat("- Characters with Lifespan Data:", sum(!is.na(lotr$lifespan) & lotr$lifespan > 0), "\n")
cat("- Mean Data Completeness:", round(mean(lotr$completeness_score, na.rm=TRUE), 2), "%\n")

cat("\nMost Common Race:", race_dist$race[1], "(", race_dist$Count[1], "characters )\n")
cat("Most Common Gender:", names(which.max(table(lotr$gender))), "\n")

cat("\n========================================\n")
cat("Analysis complete! All visualizations saved.\n")
cat("========================================\n")

# List all saved files to confirm
cat("\nGenerated files:\n")
saved_files <- list.files(pattern = "*.png")
print(saved_files)
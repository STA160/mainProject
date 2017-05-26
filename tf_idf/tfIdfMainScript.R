#used to create tf-idf csv files. You will need the data to be split up in order to use it properly
#  
#  
#  
# Randy
  
library(dplyr);library(tidytext);library(stringr)

 returnTfCongressDataName <- function(df)
 {
	 if (is.character(df$text) == FALSE)
	 {
		 innerDf <- as.character(df)
	 }
	 else
	 {
		innerDf <- df
	}
	
tidy_tempData <- innerDf %>% unnest_tokens(word, text)
data("stop_words")
cleaned_tempData <- tidy_tempData %>% anti_join(stop_words)
word_tempData <- cleaned_tempData %>% count(names,word, sort = TRUE) 	 
totalword_tempData <- word_tempData %>% group_by(names) %>% summarize(total = sum(n))
  word_tempData <- left_join(word_tempData,totalword_tempData)
  word_tempData <- word_tempData %>% bind_tf_idf(word,names,n)
  word_tempData <- word_tempData %>% select(-total) %>% arrange(desc(tf_idf))
  
	 return(word_tempData)
	 
	 
 }
 
 
  returnTfCongressDataDate <- function(df)
 {
	 if (is.character(df$text) == FALSE)
	 {
		 innerDf <- as.character(df)
	 }
	 else
	 {
		innerDf <- df
	}
	
tidy_tempData <- innerDf %>% unnest_tokens(word, text)
data("stop_words")
cleaned_tempData <- tidy_tempData %>% anti_join(stop_words)
word_tempData <- cleaned_tempData %>% count(date,word, sort = TRUE) 	 
totalword_tempData <- word_tempData %>% group_by(date) %>% summarize(total = sum(n))
  word_tempData <- left_join(word_tempData,totalword_tempData)
  word_tempData <- word_tempData %>% bind_tf_idf(word,date,n)
  word_tempData <- word_tempData %>% select(-total) %>% arrange(desc(tf_idf))
  
	 return(word_tempData)
	 
	 
 }
 
 
 
 returnTfCongressDataCongress <- function(df)
 {
	 if (is.character(df$text) == FALSE)
	 {
		 innerDf <- as.character(df)
	 }
	 else
	 {
		innerDf <- df
	}
	
tidy_tempData <- innerDf %>% unnest_tokens(word, text)
data("stop_words")
cleaned_tempData <- tidy_tempData %>% anti_join(stop_words)
word_tempData <- cleaned_tempData %>% count(congress,word, sort = TRUE) 	 
totalword_tempData <- word_tempData %>% group_by(congress) %>% summarize(total = sum(n))
  word_tempData <- left_join(word_tempData,totalword_tempData)
  word_tempData <- word_tempData %>% bind_tf_idf(word,congress,n)
  word_tempData <- word_tempData %>% select(-total) %>% arrange(desc(tf_idf))
  
	 return(word_tempData)
	 
	 
 }
 
 
  returnTfCongressDataParty <- function(df)
 {
	 if (is.character(df$text) == FALSE)
	 {
		 innerDf <- as.character(df)
	 }
	 else
	 {
		innerDf <- df
	}
	
tidy_tempData <- innerDf %>% unnest_tokens(word, text)
data("stop_words")
cleaned_tempData <- tidy_tempData %>% anti_join(stop_words)
word_tempData <- cleaned_tempData %>% count(party,word, sort = TRUE) 	 
totalword_tempData <- word_tempData %>% group_by(party) %>% summarize(total = sum(n))
  word_tempData <- left_join(word_tempData,totalword_tempData)
  word_tempData <- word_tempData %>% bind_tf_idf(word,party,n)
  word_tempData <- word_tempData %>% select(-total) %>% arrange(desc(tf_idf))
  
	 return(word_tempData)
	 
	 
 }
 
 
 
  returnTfCongressDataState <- function(df)
 {
	 if (is.character(df$text) == FALSE)
	 {
		 innerDf <- as.character(df)
	 }
	 else
	 {
		innerDf <- df
	}
	
tidy_tempData <- innerDf %>% unnest_tokens(word, text)
data("stop_words")
cleaned_tempData <- tidy_tempData %>% anti_join(stop_words)
word_tempData <- cleaned_tempData %>% count(state,word, sort = TRUE) 	 
totalword_tempData <- word_tempData %>% group_by(state) %>% summarize(total = sum(n))
  word_tempData <- left_join(word_tempData,totalword_tempData)
  word_tempData <- word_tempData %>% bind_tf_idf(word,state,n)
  word_tempData <- word_tempData %>% select(-total) %>% arrange(desc(tf_idf))
  
	 return(word_tempData)
	 
	 
 }
 
 
 
processDatedRecordsOfCongress <- function(df)
{
	mainData <- read.csv(df$file)
	mainData$text <- as.character(mainData$text)	
	
	#name
	tData <- returnTfCongressDataName(mainData)
	tString <- paste(df$year,"TF_IDF_NAME.TXT")
	write.csv(tData,tString);
	
	#date
	tData <- returnTfCongressDataDate(mainData)
	tString <- paste(df$year,"TF_IDF_DATE.TXT")
	write.csv(tData,tString);
	
	#Congress
	tData <- returnTfCongressDataCongress(mainData)
	tString <- paste(df$year,"TF_IDF_CONGRESS.TXT")
	write.csv(tData,tString);
	
	
	#Party
	tData <- returnTfCongressDataParty(mainData)
	tString <- paste(df$year,"TF_IDF_PARTY.TXT")
	write.csv(tData,tString);
	
	
	#State
	tData <- returnTfCongressDataState(mainData)
	tString <- paste(df$year,"TF_IDF_STATE.TXT")
	write.csv(tData,tString);
	
	
	
	
	rm(mainData)
}
 
#processDatedRecordsOfCongress(tmp)

 dateFile <- read.csv("dateAndFileList.csv")
 dateFile$file <- as.character(dateFile$file)
 dateFile$year <- as.character(dateFile$year)


for (val in 1:nrow(dateFile))
{
	
	
	processDatedRecordsOfCongress(dateFile[val,])
} 

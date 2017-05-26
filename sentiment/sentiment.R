# used to detect sentiment using the bing language library in tidytext
#  
#  
#  
# Randy

library(dplyr);library(tidytext);library(stringr);library(tidyr)


 
returnSentCongressData <- function(df)
{


	#this is a redundant function right here
	 if (is.character(df$text) == FALSE)
	 {
		 innerDf <- as.character(df)
	 }
	 else
	 {
		innerDf <- df
	}

	returnObject <- "" #creating an object #probably wont be used in current incarnation 
#~ 	t_Joy <- get_sentiments("nrc") 
	mainSentimentSet <-	t_Bing <- get_sentiments("bing") 
#~ 	t_Afinn <- get_sentiments("afinn")


	

	#sentiments 
	
	tidy_tempData <- innerDf %>% unnest_tokens(word, text)
	data("stop_words")
	cleaned_tempData <- tidy_tempData %>% anti_join(stop_words)
	sentiment_tempData  <- cleaned_tempData %>%
	inner_join(mainSentimentSet) %>%
	count(names,  sentiment, sort = TRUE) %>%
	#~   count(date,  sentiment, sort = TRUE) %>%
	#~   count(party,  sentiment, sort = TRUE) %>%
	#~   count(state,  sentiment, sort = TRUE) %>%
	#~   count(congress,  sentiment, sort = TRUE) %>%
	spread(sentiment, n, fill = 0) %>%
	mutate(sentiment = positive - negative)

	return(sentiment_tempData) 	

}
 
returnSentCongressDataCongress <- function(df)
{

	 if (is.character(df$text) == FALSE)
	 {
		 innerDf <- as.character(df)
	 }
	 else
	 {
		innerDf <- df
	}

	returnObject <- "" #creating an object #probably wont be used in current incarnation 
#~ 	t_Joy <- get_sentiments("nrc") 
	mainSentimentSet <-	t_Bing <- get_sentiments("bing") 
#~ 	t_Afinn <- get_sentiments("afinn")


	

	#sentiments 
	
	tidy_tempData <- innerDf %>% unnest_tokens(word, text)
	data("stop_words")
	cleaned_tempData <- tidy_tempData %>% anti_join(stop_words)
	sentiment_tempData  <- cleaned_tempData %>%
	inner_join(mainSentimentSet) %>%
#~ 	count(names,  sentiment, sort = TRUE) %>%
	#~   count(date,  sentiment, sort = TRUE) %>%
	#~   count(party,  sentiment, sort = TRUE) %>%
	#~   count(state,  sentiment, sort = TRUE) %>%
	  count(congress,  sentiment, sort = TRUE) %>%
	spread(sentiment, n, fill = 0) %>%
	mutate(sentiment = positive - negative)

	return(sentiment_tempData) 	

}
 
returnSentCongressDataParty <- function(df)
{

	 if (is.character(df$text) == FALSE)
	 {
		 innerDf <- as.character(df)
	 }
	 else
	 {
		innerDf <- df
	}

	returnObject <- "" #creating an object #probably wont be used in current incarnation 
#~ 	t_Joy <- get_sentiments("nrc") 
	mainSentimentSet <-	t_Bing <- get_sentiments("bing") 
#~ 	t_Afinn <- get_sentiments("afinn")


	

	#sentiments 
	
	tidy_tempData <- innerDf %>% unnest_tokens(word, text)
	data("stop_words")
	cleaned_tempData <- tidy_tempData %>% anti_join(stop_words)
	sentiment_tempData  <- cleaned_tempData %>%
	inner_join(mainSentimentSet) %>%
#~ 	count(names,  sentiment, sort = TRUE) %>%
	#~   count(date,  sentiment, sort = TRUE) %>%
	  count(party,  sentiment, sort = TRUE) %>%
	#~   count(state,  sentiment, sort = TRUE) %>%
	#~   count(congress,  sentiment, sort = TRUE) %>%
	spread(sentiment, n, fill = 0) %>%
	mutate(sentiment = positive - negative)

	return(sentiment_tempData) 	

}
 
returnSentCongressDataState <- function(df)
{

	 if (is.character(df$text) == FALSE)
	 {
		 innerDf <- as.character(df)
	 }
	 else
	 {
		innerDf <- df
	}

	returnObject <- "" #creating an object #probably wont be used in current incarnation 
#~ 	t_Joy <- get_sentiments("nrc") 
	mainSentimentSet <-	t_Bing <- get_sentiments("bing") 
#~ 	t_Afinn <- get_sentiments("afinn")


	

	#sentiments 
	
	tidy_tempData <- innerDf %>% unnest_tokens(word, text)
	data("stop_words")
	cleaned_tempData <- tidy_tempData %>% anti_join(stop_words)
	sentiment_tempData  <- cleaned_tempData %>%
	inner_join(mainSentimentSet) %>%
#~ 	count(names,  sentiment, sort = TRUE) %>%
	#~   count(date,  sentiment, sort = TRUE) %>%
	#~   count(party,  sentiment, sort = TRUE) %>%
	  count(state,  sentiment, sort = TRUE) %>%
	#~   count(congress,  sentiment, sort = TRUE) %>%
	spread(sentiment, n, fill = 0) %>%
	mutate(sentiment = positive - negative)

	return(sentiment_tempData) 	

}
 
returnSentCongressDataDate <- function(df)
{

	 if (is.character(df$text) == FALSE)
	 {
		 innerDf <- as.character(df)
	 }
	 else
	 {
		innerDf <- df
	}

	returnObject <- "" #creating an object #probably wont be used in current incarnation 
#~ 	t_Joy <- get_sentiments("nrc") 
	mainSentimentSet <-	t_Bing <- get_sentiments("bing") 
#~ 	t_Afinn <- get_sentiments("afinn")


	

	#sentiments 
	
	tidy_tempData <- innerDf %>% unnest_tokens(word, text)
	data("stop_words")
	cleaned_tempData <- tidy_tempData %>% anti_join(stop_words)
	sentiment_tempData  <- cleaned_tempData %>%
	inner_join(mainSentimentSet) %>%
#~ 	count(names,  sentiment, sort = TRUE) %>%
	  count(date,  sentiment, sort = TRUE) %>%
	#~   count(party,  sentiment, sort = TRUE) %>%
	#~   count(state,  sentiment, sort = TRUE) %>%
	#~   count(congress,  sentiment, sort = TRUE) %>%
	spread(sentiment, n, fill = 0) %>%
	mutate(sentiment = positive - negative)

	return(sentiment_tempData) 	

}
 
 
returnSentCongressDataName <- function(df)
{

	 if (is.character(df$text) == FALSE)
	 {
		 innerDf <- as.character(df)
	 }
	 else
	 {
		innerDf <- df
	}

	returnObject <- "" #creating an object #probably wont be used in current incarnation 
#~ 	t_Joy <- get_sentiments("nrc") 
	mainSentimentSet <-	t_Bing <- get_sentiments("bing") 
#~ 	t_Afinn <- get_sentiments("afinn")


	

	#sentiments 
	
	tidy_tempData <- innerDf %>% unnest_tokens(word, text)
	data("stop_words")
	cleaned_tempData <- tidy_tempData %>% anti_join(stop_words)
	sentiment_tempData  <- cleaned_tempData %>%
	inner_join(mainSentimentSet) %>%
	count(names,  sentiment, sort = TRUE) %>%
	#~   count(date,  sentiment, sort = TRUE) %>%
	#~   count(party,  sentiment, sort = TRUE) %>%
	#~   count(state,  sentiment, sort = TRUE) %>%
	#~   count(congress,  sentiment, sort = TRUE) %>%
	spread(sentiment, n, fill = 0) %>%
	mutate(sentiment = positive - negative)

	return(sentiment_tempData) 	

}
 


##Computations begine here:: 

processSentimentDatedRecordsOfCongress <- function(df)
{
	mainData <- read.csv(df$file)
	mainData$text <- as.character(mainData$text)	
	
	#name
	tData <- returnSentCongressDataName(mainData)
	tString <- paste(df$year,"SENT_NAME.TXT")
	write.csv(tData,tString);
	
	#date
	tData <- returnSentCongressDataDate(mainData)
	tString <- paste(df$year,"SENT_DATE.TXT")
	write.csv(tData,tString);
	
	#Congress
	tData <- returnSentCongressDataCongress(mainData)
	tString <- paste(df$year,"SENT_CONGRESS.TXT")
	write.csv(tData,tString);
	
	
	#Party
	tData <- returnSentCongressDataParty(mainData)
	tString <- paste(df$year,"SENT_PARTY.TXT")
	write.csv(tData,tString);
	
	
	#State
	tData <- returnSentCongressDataState(mainData)
	tString <- paste(df$year,"SENT_STATE.TXT")
	write.csv(tData,tString);
	
	
	
	
	rm(mainData)
}
 
#processDatedRecordsOfCongress(tmp)

 dateFile <- read.csv("dateAndFileList.csv")
 dateFile$file <- as.character(dateFile$file)
 dateFile$year <- as.character(dateFile$year)


for (val in 1:nrow(dateFile))
{
	
	
	processSentimentDatedRecordsOfCongress(dateFile[val,])
} 

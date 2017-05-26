library(dplyr);library(tidytext);library(stringr);library(tidyr)


#~ t_Joy <- get_sentiments("nrc") 
#~ t_Bing <- get_sentiments("bing") 
#~ t_Afinn <- get_sentiments("afinn")


  
#~   <- cleaned2017Data %>%
#~   inner_join(bing) %>%
#~   count(names,  sentiment, sort = TRUE) %>%
#~   count(date,  sentiment, sort = TRUE) %>%
#~   count(party,  sentiment, sort = TRUE) %>%
#~   count(state,  sentiment, sort = TRUE) %>%
#~   count(congress,  sentiment, sort = TRUE) %>%
#~   spread(sentiment, n, fill = 0) %>%
#~   mutate(sentiment = positive - negative)
  
  
#~   processSentimentCongress
  
  
#~     returnTfCongressDataState <- function(df)
#~  {
#~ 	 if (is.character(df$text) == FALSE)
#~ 	 {
#~ 		 innerDf <- as.character(df)
#~ 	 }
#~ 	 else
#~ 	 {
#~ 		innerDf <- df
#~ 	}
	
#~ #word_tempData <- cleaned_tempData %>% count(state,word, sort = TRUE) 	 
#~ #totalword_tempData <- word_tempData %>% group_by(state) %>% summarize(total = sum(n))
#~   word_tempData <- left_join(word_tempData,totalword_tempData)
#~   word_tempData <- word_tempData %>% bind_tf_idf(word,state,n)
#~   word_tempData <- word_tempData %>% select(-total) %>% arrange(desc(tf_idf))
  
#~ 	 return(word_tempData)
	 
	 
#~  }
 
 
 
 
returnSentCongressData <- function(df)
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
 
 
returnSentCongressDataNames <- function(df)
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
 

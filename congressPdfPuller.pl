#!/usr/bin/perl

#congress puller
#this script pulls the congressional records. It could have been done in bash, but I use perl since I'm more formal with it
# it creates the congressional records url through deterministic strings, and then downloads using wget

my $mainUrlTemp = "https://www.congress.gov/crec/2017/04/24/CREC-2017-04-24.pdf"; #deprecated

my $yearNum = 1995; #year variable
my $monthNum = 0; #month variable
my $dayNum = 0; #day variable

#~ sub returnFormattedDay($); 
my $innerDayNumString = "";  #inner loop string
my $innerMonthNumString = "";  #month number string

my $mainUrlString = ""; #this is the main url string right here

for ($yearNum = 1995; $yearNum < 2018; $yearNum++)
{
	#outer year loop
	for($monthNum = 1; $monthNum < 13; $monthNum++)
	{
		#month loop
		for($dayNum = 1; $dayNum < 32; $dayNum++)
		{
			#day loop if statement is used for string adjustment in days

			if ($dayNum < 10) 
			{
				#~ $innerMonthNumString = '0' . $monthNum; 
				$innerDayNumString = '0' . $dayNum; 
			
			}
			else
			{
				#~ $innerMonthNumString = $monthNum; 
				$innerDayNumString = $dayNum; 
				
				
			}
			
			if ($monthNum < 10)
			{
					$innerMonthNumString = '0' . $monthNum; 
			}
			else
			{
				
				$innerMonthNumString = $monthNum;
			}
			
			$mainUrlString =	'https://www.congress.gov/crec/'. $yearNum .'/'.$innerMonthNumString.'/'.$innerDayNumString.'/CREC-'.$yearNum.'-'.$innerMonthNumString.'-'. $innerDayNumString .'.pdf'; #main url string formatted
			#~ print $mainUrlString . "\n"; 
			`wget $mainUrlString`; #getting the data with wget command line tool
			#~ print $innerMonthNumString . "\n"; 
			#~ print $innerDayNumString . "\n"; 
			
			
			#~ $innerMonthNumString; 
				#~ $innerDayNumString
		}
	
	}
	
}



#~ sub returnFormattedDay($);

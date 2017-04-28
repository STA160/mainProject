#!/usr/bin/perl

#congress puller

my $mainUrlTemp = "https://www.congress.gov/crec/2017/04/24/CREC-2017-04-24.pdf";

my $yearNum = 1995; 
my $monthNum = 0;
my $dayNum = 0;

#~ sub returnFormattedDay($); 
my $innerDayNumString = ""; 
my $innerMonthNumString = ""; 

my $mainUrlString = ""; #this is the main url string right here

for ($yearNum = 1995; $yearNum < 2018; $yearNum++)
{
	for($monthNum = 1; $monthNum < 13; $monthNum++)
	{
		
		for($dayNum = 1; $dayNum < 32; $dayNum++)
		{
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
			
			$mainUrlString =	'https://www.congress.gov/crec/'. $yearNum .'/'.$innerMonthNumString.'/'.$innerDayNumString.'/CREC-'.$yearNum.'-'.$innerMonthNumString.'-'. $innerDayNumString .'.pdf';
			#~ print $mainUrlString . "\n"; 
			`wget $mainUrlString`; #getting the data
			#~ print $innerMonthNumString . "\n"; 
			#~ print $innerDayNumString . "\n"; 
			
			
			#~ $innerMonthNumString; 
				#~ $innerDayNumString
		}
	
	}
	
}



#~ sub returnFormattedDay($);

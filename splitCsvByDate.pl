#!/usr/bin/perl

# This script is a tool that takes the big csv file and splits it by dates
#
#


use strict;
use warnings; 

my $yearIndice = ""; #year variable


my $fileHandle; #deprecated
my @mainFile = <>;  #input on commmand line. Pass it the main csv file
my $tempLine = ""; #just a buffer
my @splitArray; #array used to split

for ( my $date = 2006; $date < 2018; $date++)
{
	#outer loop, for a range of dates 2006 to 2017
	open('FILE',"> $date.sortedOutput.csv"); #open the fd or die
	
	print FILE ",congress,date,end_year,names,party,start_year,state,text\n"; 
	
	for (my $i = 0; $i < @mainFile; $i++)
	{
		$tempLine = $mainFile[$i]; #temp variable... much cleaner
		@splitArray = split(',',$tempLine); #split by commas
	
		if ($splitArray[2] =~ m/$date/) #match for the given date
		{
			print FILE $tempLine; #output to text file
			#~ print $splitArray[2] . "\n";

		
		}
		#~ print $splitArray[2] . "\n";

	}

	close(FILE); #close file handle

}
 





#!/usr/bin/perl

# This script is a tool that takes the big csv file and splits it by dates
#
#


use strict;
use warnings; 

my $yearIndice = ""; 


my $fileHandle;
my @mainFile = <>; 
my $tempLine = ""; 
my @splitArray; 

for ( my $date = 2006; $date < 2018; $date++)
{
	open('FILE',"> $date.sortedOutput.txt"); #open the fd or die
	
	print FILE ",congress,date,end_year,names,party,start_year,state,text\n"; 
	
	for (my $i = 0; $i < @mainFile; $i++)
	{
		$tempLine = $mainFile[$i];
		@splitArray = split(',',$tempLine); 
	
		if ($splitArray[2] =~ m/$date/)
		{
			print FILE $tempLine; 
			#~ print $splitArray[2] . "\n";

		
		}
		#~ print $splitArray[2] . "\n";

	}

	close(FILE); 

}
 





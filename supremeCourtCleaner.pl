#!/usr/bin/perl

use strict; 
use warnings; 


#this cleans the supreme court records. 
#This script is
#~ my $file = $ARGV[0] or die "file input not selected!\n";
my $myPDF = $ARGV[0] or die "file input not selected!\n";
my $endString = "The case is submitted.";
my @mainFileArray;
#grab pdf 

`pdftotext $myPDF`; #
$myPDF =~ s/\.pdf/\.txt/g; #turn .pdf file extension to .txt 
						#~ $ifString =~ s/elif/if (/;
open('FILE',"< $myPDF") or die "error creating output file" ; #open the fd or die

#main mean of file

while(<FILE>)
{
	
		if($_)
		{
	
			$_ =~ s/[0-9]:*[0-9]/\n/g; ##
			$_ =~ s/[0-9]*[0-9]/\n/g; ##
			
			
			chomp($_); #chomping out the new line
			next if /^\s*($|#)/; #get out blank lines
			next if m/Alderson Reporting Company/; #get out blank lines
			next if m/Official - Subject to Final Review/; #get out blank lines
			
			if ($_ =~ m/$endString/)
			{
				goto PROCESS_DATA; 
			}
			
			
				
			
			
			push(@mainFileArray,$_);
		}
	
	
	
	
}

PROCESS_DATA: 

close(FILE); #closing the file right here 

#array is post processed 

`rm $myPDF`; #remove file to save space


my $i = 0; 

for ($i = 0; $i < @mainFileArray; $i++)
{
	
	print $mainFileArray[$i] . "\n"; 
		
	
	#end of for loop
}




exit 0; #exit the main program

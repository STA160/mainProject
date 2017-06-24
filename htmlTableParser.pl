#!/usr/bin/perl

#~ use strict;
use warnings; 

##You will need to download the two bottom packages from CPAN
use HTML::TableExtract;
use Text::Table;

##
# This script will parse the modified html file and then output the popularity data as a csv in order to run computations 
#
# This script outputs to stdout, using a '>' redirection is recommmended to create a file
##

my $doc = 'cleanedTableData.html'; #the filename

my $headers =  [ 'State Name', 'Approve', 'Disapprove', 'Senator', 'Party' ]; #headers to look for in html file
 
my $table_extract = HTML::TableExtract->new(headers => $headers); #instantiating an obeject from headers extraction 
my $table_output = Text::Table->new(@$headers); #instantiate a new object for output 
 
$table_extract->parse_file($doc); #parse file
my ($table) = $table_extract->tables;

print @$headers[0] . ',' . @$headers[1] . ',' . @$headers[2] . ',' . @$headers[3] . ',' . @$headers[4] . ',' .  "Name"; #print initial headers of csv
print "\n"; #newline

my @nuSenatorName; #this adds a new name to upper case so we can better grep the name in R



#~ 
#~ my $tempString; 
for my $row ($table->rows) {
    #~ clean_up_spaces($row); # not shown for brevity
    #~ $tempString = @$row[3]; 
    
	@nuSenatorName = split(' ', @$row[3]); #this is the split name right here
	#translate to something else
	
	#strip the percents of the value strings, and just leave the numbers 
	 

	@$row[1] =~ s/%//g; #turn % into blank
	@$row[2] =~ s/%//g; #turn % into blank
	
    print @$row[0] . ',' . @$row[1] . ',' . @$row[2] . ',' . @$row[3] . ',' . @$row[4] . ',' . uc ($nuSenatorName[1]); #prints the csv records
    #~ print $tempString .  "\n";
    print "\n";
    #~ $table_output->load($row);
}

#done

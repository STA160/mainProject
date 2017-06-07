use HTML::TableExtract;
use Text::Table;
use HTML::TableExtract;
use WWW::Mechanize;
#~ use strict;

my $doc = 'cleanedTableData.html';

my $headers =  [ 'State Name', 'Approve', 'Disapprove', 'Senator', 'Party' ];
 
my $table_extract = HTML::TableExtract->new(headers => $headers);
my $table_output = Text::Table->new(@$headers);
 
$table_extract->parse_file($doc);
my ($table) = $table_extract->tables;

print @$headers[0] . ',' . @$headers[1] . ',' . @$headers[2] . ',' . @$headers[3] . ',' . @$headers[4];
print "\n";


for my $row ($table->rows) {
    #~ clean_up_spaces($row); # not shown for brevity
    print @$row[0] . ',' . @$row[1] . ',' . @$row[2] . ',' . @$row[3] . ',' . @$row[4];
    print "\n";
    #~ $table_output->load($row);
}
 
#~ print $table_output;


#~ $table_output =~ s//,/g;


#~ print $table_output;

CREATE EXTENSION jsonb_plperlu CASCADE;

CREATE FUNCTION test1(val jsonb) RETURNS jsonb
LANGUAGE plperlu
TRANSFORM FOR TYPE jsonb
AS $$
return (%_[0]);
$$;

CREATE FUNCTION test2(val text) RETURNS text
LANGUAGE plperlu
AS $$
use JSON;
my $hash = decode_json($_[0]);
return encode_json $hash;
$$;

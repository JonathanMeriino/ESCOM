library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity fulladder is
	Port(cin: in STD_LOGIC;
	       a: in STD_LOGIC;
	       b: in STD_LOGIC;
	       s: out STD_LOGIC;
	      cout: out STD_LOGIC);	
end fulladder;

architecture Behavioral of fulladder is
begin

s<= <a xor b xor cin;
cout<=(a and b) or(cin and (a or b);

end Behavorial;

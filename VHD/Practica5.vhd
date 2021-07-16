library ieee;
use ieee.std_logic_1164.all;

entity practica5 is 
port(clock, rst, A : in std_logic;
	B : out  std_logic);
end practica5;

architecture Behavioral of practica5 is 

begin 

process(clock)

begin
	if clock'event and clock ='1' then 
		if rst='1' then
		B <='0';
		else 
			B <= A;
		end if;
	end if;
end process;


end Behavioral;
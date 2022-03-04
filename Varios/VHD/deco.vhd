library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity decodificador is
	Port(entrada : in STD_LOGIC_VECTOR (2 downto 0);
	salida : out STD_LOGIC_VECTOR(7 downto 0);
	en : in STD_LOGIC);

end decodificador;

architecture funcionamiento of decodificador is

begin

	process(entrada,en)
	begin
	case entrada is 
	when "000"=>
	 	if en= '1' then 
			salida <= "10000000";
		else 
			salida <="0000000";
		
		 end if;
	when"001" =>
		if en = '1' then 
			salida <= "01000000";
		else
			salida <="0000000";
	end if;

	when"010" =>
		if en ='1' then 
			salida <= "00100000";
		else
			salida <="00000000";
		end if;

	when "011" =>
		if en ='1' then
			salida <= "00010000";
		else
			salida<= "00000000";
	
		end if;


	when "100" =>
		if en='1' then
			salida<= "00001000";

		else
			salida<= "00000000";
		end if;

	when "101" =>
		if en ='1' then
			salida<= "000000100";
		else
			salida<= "00000000" ;
		end if;

	when "110" =>
		if en='1' then
			salida<= "0000000010" ;
		else
			salida<= "00000000";
		end if;

	when "111" =>
		if en='1' then 
			salida<="000000001";
		else
			salida<= "00000000";
		end if;
	when others =>
		salida<= "000000000";
	end case;

end funcionamiento;

-- mario que salta el piso 
library ieee;
use ieee.std_logic_1164.all;

entity mario_en is
	Port (
			clk: in bit;
			sen: inout bit;  -- señal
			enable: in bit;   -- enable
			mario_adv:inout bit;	--avanzar
			posicion:inout bit_vector(0 to 7) -- muestra la salida
			);

end mario_en;

architecture mario_arq of  mario_en is

signal vec_mario:  bit_vector(0 to 7 ):="10000000"; -- vector mario
signal en_mario : bit:='1';   -- mueve el circuito, meten datos de manera seriada, recorrer datos
signal fn_mario  :bit: -'0';
	
signal vec_tort:  bit_vector(0 to 7 ):="00000001"; -- vector tortuga
signal en_tort  : bit:='0';
signal fn_tort  :bit :- '1' ;


	begin

	process(enable,vec_tort, clk,sen,en_mario,fn_mario,vec_mario) -- reset señal sensitiva
		begin
		if clk'event and clk='1' then
				if(enable='1') then
						vec_mario <= "00000000";
						vec_tort <= "00000000";
				else
				--mueve vector tortuga
				    vec_tort(0) <= (sen and en_mario) or (fn_mario and vec_tort(1));

			for i in 1 to 6 loop

				vec_tort(i) <= (vec_tort(i-1) and en_tort) or (fn_tort and vec_tort(i+1));
		        
			end loop;
		        
			vec_tort(7) <= (vec_tort(6) and en_tort) or (fn_tort and sen);
			--termina movimiento tortuga
			
			if (mario_adv ='1') then
			--mueve vector mario
				vec_mario(0) <= (sen and en_mario) or (fn_mario and vec_mario(1));

	        for i in 1 to 6 loop

				vec_mario(i) <= (vec_mario(i-1) and en_mario) or (fn_mario and vec_mario(i+1));

	        end loop;
	        		vec_mario(7) <= (vec_mario(6) and en_mario) or (fn_mario and sen);
			--termina vector mario
			else
			    vec_mario <= vec_mario; -- guardar el dato sin perderlo
		 	end if ;
		end if;
		for i in 0 to 6 loop
			if (posicion(i) and posicion(i+1)) = '1' then
					-- reinicia el valor
					vec_tort <="00000000";
		    		vec_mario<= "00000000";
			end if ;
	   	end loop;
	    	end if;
	    	posicion <= (vec_mario or vec_tort); -- vector que suma

	end process;

	process (vec_mario) -- si no existe un mario, lo agrega 

		begin
			if ((vec_mario(0)or vec_mario(1)or vec_mario(2)or vec_mario(3)or vec_mario(4)or vec_mario(5)or vec_mario(6)or vec_mario(7))='0') then -- suma las señales de los vectores
				sen<='1';

			else

    			sen<='0';

			end if;

	end process;



end architecture;

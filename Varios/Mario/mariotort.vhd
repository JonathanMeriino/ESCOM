-- Este codigo crea un mario con una tortuga
library ieee;
use ieee.std_logic_1164.all;

entity mario_en is
	Port (
			clk: in std_logic;
			sen: inout bit;  -- señal
			enable: in bit;   -- enable
			mario_adv:inout bit;	--avanzar
			posicion:inout bit_vector(0 to 7); -- muestra la salida
			sal_boton:inout bit;
			piso: inout bit_vector(0 to 7)
			);

end mario_en;

architecture mario_arq of  mario_en is

signal vec_mario:  bit_vector(0 to 7 ):="10000000"; -- vector mario
signal en_mario : bit:='1';   -- mueve el circuito, meten datos de manera seriada, recorrer datos
signal fn_mario : bit:='0';

signal vec_tort:  bit_vector(0 to 7 ):="00000001"; -- vector tortuga
signal en_tort  : bit:='0'; 
signal fn_tort  : bit:= '1';

signal mariojump: bit_vector(0 to 7 );
signal knoptsal: bit:='0';



	begin

	process(enable,vec_tort, clk,sen,en_mario,fn_mario,vec_mario) -- reset señal sensitiva
		begin
		if rising_edge(clk) then    -- retrasa el evento
				if(enable='1') then
						vec_mario <= "00000000";
						vec_tort <= "00000000";
						piso<="00000000";
				else
				piso<="11111111";
				--mueve vector tortuga
				    vec_tort(0) <= (sen and en_tort) or (fn_tort and vec_tort(1));

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


       -- primer salto vertical 
		if (Sal_boton='1'and mario_adv='0') then
			knoptsal<='1';  -- bandera para que baje automaticamente
			mariojump <= vec_mario;  -- guarda dato del mario
			vec_mario<= "00000000"; -- vector mario manda a 0
		-- salto diagonal
		elsif (Sal_boton='1'and mario_adv='1') then
			knoptsal<='1'; -- bandera toma el valor de 1
			
			-- Se mueve una posicion y se guarda en mariojumo
			mariojump (0) <= (sen and en_mario) or (fn_mario and vec_mario(1)); 

			for i in 1 to 6 loop

				mariojump(i) <= (vec_mario(i-1) and en_mario) or (fn_mario and vec_mario(i+1));

			end loop;
		mariojump (7) <= (vec_mario(6) and en_mario) or (fn_mario and sen);
			-- termina el proceso

		vec_mario <= "00000000"; -- mandamos a ceros para no tener dos marios

		end if ;

		-- baja salto vertical
		if (knoptsal = '1'and mario_adv='0') then
			vec_mario <= mariojump; -- baja en la misma posicion
			mariojump <= "00000000"; -- manda a 0s para que no existan dos marios
			knoptsal <= '0'; -- mando la bandera a cero
			sal_boton <= '0'; -- manda el boton saltar a cero retrasandolo 1 proceso clk
		
		-- baja mi salto diagonal
		elsif(knoptsal = '1' and mario_adv='1')then
			vec_mario(0) <= (sen and en_mario) or (fn_mario and mariojump(1)); -- mueve una posicion y la guarda

				for i in 1 to 6 loop

			vec_mario(i) <= (mariojump(i-1) and en_mario) or (fn_mario and mariojump(i+1));

				end loop;
						vec_mario(7) <= (mariojump(6) and en_mario) or (fn_mario and sen);
		-- termina el proceso de mover y guardar				
		mariojump <= "00000000"; -- manda el mario a cero para que no existan dos
		knoptsal <= '0'; -- manda la bandera a cero 
		sal_boton <= '0'; -- manda el boton de saltar a cero

		end if;




		-- la muerte de mario
		for i in 0 to 6 loop
			-- condicion para saber si estan en la misma posicion
			if ((((vec_mario(i) and vec_tort(i+1) )or (vec_mario(i) and vec_tort(i))) = '1')and Sal_boton ='0') then
					-- vuelve a posciones iniciales
					vec_tort <="00000001";
		    		vec_mario<= "10000000";
			end if ;
	   	end loop;
		-- fin del proceso
					-- muerte de la tortuga
						if  Sal_boton='1' then
									if mario_adv ='1'then
										-- muerte de la tortuga en diagonal
										for i in 0 to 6 loop
											if ((mariojump(i) and vec_tort(i+1))='1') then
												vec_tort <="00000000";
											end if;
										end loop;
									else
										-- muerte con salto vertical
										for i in 0 to 6 loop
											if ((mariojump(i) and vec_tort(i))='1') then
												vec_tort <="00000000"; -- manda la tortuga a ceros
											end if;
										end loop;
									end if;

								end if ;
	    				end if;
	    	posicion <= (vec_mario or vec_tort); -- vector que suma

	end process;

	process (vec_mario,sal_boton) -- si no existe un mario, lo agrega

		begin
			if ((vec_mario(0)or vec_mario(1)or vec_mario(2)or vec_mario(3)or vec_mario(4)or vec_mario(5)or vec_mario(6)or vec_mario(7)or Sal_boton )='0') then -- suma las señales de los vectores
				sen<='1';

			else

    			sen<='0';

			end if;

	end process;



end architecture;

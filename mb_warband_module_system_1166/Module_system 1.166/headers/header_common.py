###################################################
# header_common.py
# This file contains common declarations.
# DO NOT EDIT THIS FILE!
###################################################

#client events
multiplayer_event_set_item_selection                          = 0
multiplayer_event_set_bot_selection                           = 1
multiplayer_event_admin_start_map                             = 2
multiplayer_event_admin_set_max_num_players                   = 3
multiplayer_event_admin_set_num_bots_in_team                  = 4
multiplayer_event_admin_set_friendly_fire                     = 5
multiplayer_event_admin_set_ghost_mode                        = 6
multiplayer_event_admin_set_control_block_dir                 = 7
multiplayer_event_admin_set_add_to_servers_list               = 8
multiplayer_event_admin_set_respawn_period                    = 9
multiplayer_event_admin_set_game_max_minutes                  = 10
multiplayer_event_admin_set_round_max_seconds                 = 11
multiplayer_event_admin_set_game_max_points                   = 12
multiplayer_event_admin_set_point_gained_from_flags           = 13
multiplayer_event_admin_set_point_gained_from_capturing_flag  = 14
multiplayer_event_admin_set_server_name                       = 15
multiplayer_event_admin_set_game_password                     = 16
multiplayer_event_admin_set_team_faction                      = 17
multiplayer_event_open_admin_panel                            = 18
multiplayer_event_change_team_no                              = 19
multiplayer_event_change_troop_id                             = 20
multiplayer_event_start_new_poll                              = 21
multiplayer_event_answer_to_poll                              = 22
multiplayer_event_admin_kick_player                           = 23
multiplayer_event_admin_ban_player                            = 24
multiplayer_event_admin_set_num_bots_voteable                 = 25
multiplayer_event_admin_set_factions_voteable                 = 26
multiplayer_event_admin_set_maps_voteable                     = 27
multiplayer_event_admin_set_player_respawn_as_bot             = 28
multiplayer_event_admin_set_combat_speed                      = 29
multiplayer_event_admin_set_respawn_count                     = 30
multiplayer_event_admin_set_kick_voteable                     = 31
multiplayer_event_admin_set_ban_voteable                      = 32
multiplayer_event_admin_set_valid_vote_ratio                  = 33
multiplayer_event_admin_set_auto_team_balance_limit           = 34
multiplayer_event_admin_set_welcome_message                   = 35
multiplayer_event_admin_set_initial_gold_multiplier           = 36
multiplayer_event_admin_set_battle_earnings_multiplier        = 37
multiplayer_event_admin_set_round_earnings_multiplier         = 38
multiplayer_event_admin_set_melee_friendly_fire               = 39
multiplayer_event_admin_set_friendly_fire_damage_self_ratio   = 40
multiplayer_event_admin_set_friendly_fire_damage_friend_ratio = 41
multiplayer_event_admin_set_allow_player_banners              = 42
multiplayer_event_admin_set_force_default_armor               = 43
multiplayer_event_admin_set_anti_cheat                        = 44
multiplayer_event_open_game_rules                             = 45
multiplayer_event_offer_duel                                  = 46
multiplayer_event_admin_set_disallow_ranged_weapons           = 47

#server events
multiplayer_event_return_max_num_players                      = 50
multiplayer_event_return_num_bots_in_team                     = 51
multiplayer_event_return_friendly_fire                        = 52
multiplayer_event_return_ghost_mode                           = 53
multiplayer_event_return_control_block_dir                    = 54
multiplayer_event_return_combat_speed                         = 55
multiplayer_event_return_add_to_servers_list                  = 56
multiplayer_event_return_respawn_period                       = 57
multiplayer_event_return_game_max_minutes                     = 58
multiplayer_event_return_round_max_seconds                    = 59
multiplayer_event_return_game_max_points                      = 60
multiplayer_event_return_point_gained_from_flags              = 61
multiplayer_event_return_point_gained_from_capturing_flag     = 62
multiplayer_event_return_server_name                          = 63
multiplayer_event_return_game_password                        = 64
multiplayer_event_return_game_type                            = 65
multiplayer_event_return_confirmation                         = 66
multiplayer_event_return_rejection                            = 67
multiplayer_event_show_multiplayer_message                    = 68
multiplayer_event_draw_this_round                             = 69
multiplayer_event_set_attached_scene_prop                     = 70
multiplayer_event_set_team_flag_situation                     = 71
multiplayer_event_set_team_score                              = 72
multiplayer_event_set_num_agents_around_flag                  = 73
multiplayer_event_ask_for_poll                                = 74
multiplayer_event_change_flag_owner                           = 75
multiplayer_event_use_item                                    = 76
multiplayer_event_set_scene_prop_open_or_close                = 77
multiplayer_event_set_round_start_time                        = 78
multiplayer_event_force_start_team_selection                  = 79
multiplayer_event_start_death_mode                            = 80
multiplayer_event_return_num_bots_voteable                    = 81
multiplayer_event_return_factions_voteable                    = 82
multiplayer_event_return_maps_voteable                        = 83
multiplayer_event_return_next_team_faction                    = 84
multiplayer_event_return_player_respawn_as_bot                = 85
multiplayer_event_set_player_score_kill_death                 = 86
multiplayer_event_set_day_time                                = 87
multiplayer_event_return_respawn_count                        = 88
multiplayer_event_return_player_respawn_spent                 = 89
multiplayer_event_return_kick_voteable                        = 90
multiplayer_event_return_ban_voteable                         = 91
multiplayer_event_return_valid_vote_ratio                     = 92
multiplayer_event_return_auto_team_balance_limit              = 93
multiplayer_event_return_initial_gold_multiplier              = 94
multiplayer_event_return_battle_earnings_multiplier           = 95
multiplayer_event_return_round_earnings_multiplier            = 96
multiplayer_event_return_renaming_server_allowed              = 97
multiplayer_event_return_changing_game_type_allowed           = 98
multiplayer_event_return_melee_friendly_fire                  = 99
multiplayer_event_return_friendly_fire_damage_self_ratio      = 100
multiplayer_event_return_friendly_fire_damage_friend_ratio    = 101
multiplayer_event_return_allow_player_banners                 = 102
multiplayer_event_return_force_default_armor                  = 103
multiplayer_event_return_anti_cheat                           = 104
multiplayer_event_return_open_game_rules                      = 105
multiplayer_event_return_max_num_bots                         = 106
multiplayer_event_return_server_mission_timer_while_player_joined = 107
multiplayer_event_show_duel_request                           = 108
multiplayer_event_start_duel                                  = 109
multiplayer_event_cancel_duel                                 = 110
multiplayer_event_show_server_message                         = 111
multiplayer_event_return_disallow_ranged_weapons              = 112

# Truand Brawl multiplayer events
multiplayer_event_boost_damage = 113

#multiplayer message types
multiplayer_message_type_auto_team_balance_done      = 2
multiplayer_message_type_auto_team_balance_next      = 3
multiplayer_message_type_capture_the_flag_score      = 4
multiplayer_message_type_flag_returned_home          = 5
multiplayer_message_type_capture_the_flag_stole      = 6
multiplayer_message_type_poll_result                 = 7
multiplayer_message_type_flag_neutralized            = 8
multiplayer_message_type_flag_captured               = 9
multiplayer_message_type_flag_is_pulling             = 10
multiplayer_message_type_auto_team_balance_no_need   = 11
multiplayer_message_type_round_result_in_battle_mode = 12
multiplayer_message_type_round_result_in_siege_mode  = 13
multiplayer_message_type_round_draw                  = 14
multiplayer_message_type_target_destroyed            = 15
multiplayer_message_type_defenders_saved_n_targets   = 16
multiplayer_message_type_attackers_won_the_round     = 17
multiplayer_message_type_start_death_mode            = 18

#multiplayer game type indices
multiplayer_game_type_deathmatch             = 0
multiplayer_game_type_team_deathmatch        = 1
multiplayer_game_type_battle                 = 2
multiplayer_game_type_destroy                = 3
multiplayer_game_type_capture_the_flag       = 4
multiplayer_game_type_headquarters           = 5
multiplayer_game_type_siege                  = 6
multiplayer_game_type_duel                   = 7
multiplayer_num_game_types                   = 8

#admin panel value ranges
multiplayer_round_max_seconds_min            = 60
multiplayer_round_max_seconds_max            = 901
multiplayer_respawn_period_min               = 3
multiplayer_respawn_period_max               = 31 #can only be 30 seconds max (due to agent deletion after that period)

multiplayer_siege_mod_defender_team_extra_respawn_time = 27 #It was 20 in 1.113 but it is increased it to 25 in 1.121 because defenders were mostly defeating enemy.
multiplayer_new_agents_finish_spawning_time = 30
multiplayer_max_possible_player_id = 1000

#team 1 and team 2 are 0 and 1 respectively
multi_team_spectator = 2
multi_team_unassigned = multi_team_spectator + 1

multi_data_maps_for_game_type_begin = 0
multi_data_maps_for_game_type_end = multi_data_maps_for_game_type_begin + 30
multi_data_troop_button_indices_begin = multi_data_maps_for_game_type_end
multi_data_troop_button_indices_end = multi_data_troop_button_indices_begin + 16 #maximum 16 troops per faction
multi_data_item_button_indices_begin = multi_data_troop_button_indices_end
multi_data_item_button_indices_end = multi_data_item_button_indices_begin + 100 #maximum 100 items per troop
multi_data_flag_owner_begin = multi_data_item_button_indices_end
multi_data_flag_owner_end = multi_data_flag_owner_begin + 10 #maximum of 10 flags per scene
multi_data_flag_players_around_begin = multi_data_flag_owner_end 
multi_data_flag_players_around_end = multi_data_flag_players_around_begin + 10 #maximum of 10 flags per scene
multi_data_flag_owned_seconds_begin = multi_data_flag_players_around_end
multi_data_flag_owned_seconds_end = multi_data_flag_owned_seconds_begin + 10 #maximum of 10 flags per scene
multi_data_flag_pull_code_begin = multi_data_flag_owned_seconds_end
multi_data_flag_pull_code_end = multi_data_flag_pull_code_begin + 10 #maximum of 10 flags per scene
multi_data_player_index_list_begin = multi_data_flag_pull_code_end

#Entry points 100..109 is used for showing initial points for moveable and usable scene props like siege ladder.
multi_entry_points_for_usable_items_start = 100
multi_entry_points_for_usable_items_end = multi_entry_points_for_usable_items_start + 10


#multi_item_class_type_other = 0
multi_item_class_type_sword = 1
multi_item_class_type_axe = 2
multi_item_class_type_blunt = 3
multi_item_class_type_war_picks = 4
multi_item_class_type_cleavers = 5
multi_item_class_type_two_handed_sword = 6
multi_item_class_type_two_handed_axe = 7
multi_item_class_type_spear = 8
multi_item_class_type_lance = 9
multi_item_class_type_small_shield = 10
multi_item_class_type_large_shield = 11
multi_item_class_type_bow = 12
multi_item_class_type_crossbow = 13
multi_item_class_type_arrow = 14
multi_item_class_type_bolt = 15
multi_item_class_type_throwing = 16
multi_item_class_type_throwing_axe = 17
multi_item_class_type_horse = 18
multi_item_class_type_light_armor = 19
multi_item_class_type_medium_armor = 20
multi_item_class_type_heavy_armor = 21
multi_item_class_type_light_helm = 22
multi_item_class_type_heavy_helm = 23
multi_item_class_type_light_foot = 24
multi_item_class_type_heavy_foot = 25
multi_item_class_type_glove = 26

multi_item_class_type_melee_weapons_begin = multi_item_class_type_sword
multi_item_class_type_melee_weapons_end = multi_item_class_type_small_shield
multi_item_class_type_ranged_weapons_begin = multi_item_class_type_bow
multi_item_class_type_ranged_weapons_end = multi_item_class_type_horse
multi_item_class_type_shields_begin = multi_item_class_type_melee_weapons_end
multi_item_class_type_shields_end = multi_item_class_type_bow

multi_item_class_type_weapons_begin = multi_item_class_type_sword
multi_item_class_type_weapons_end = multi_item_class_type_horse
multi_item_class_type_horses_begin = multi_item_class_type_weapons_end
multi_item_class_type_horses_end = multi_item_class_type_light_armor
multi_item_class_type_bodies_begin = multi_item_class_type_horses_end
multi_item_class_type_bodies_end = multi_item_class_type_light_helm
multi_item_class_type_heads_begin = multi_item_class_type_bodies_end
multi_item_class_type_heads_end = multi_item_class_type_light_foot
multi_item_class_type_feet_begin = multi_item_class_type_heads_end
multi_item_class_type_feet_end = multi_item_class_type_glove
multi_item_class_type_gloves_begin = multi_item_class_type_feet_end
multi_item_class_type_gloves_end = multi_item_class_type_glove + 1

multi_troop_class_other = 0
multi_troop_class_infantry = 1
multi_troop_class_spearman = 2
multi_troop_class_cavalry = 3
multi_troop_class_archer = 4
multi_troop_class_crossbowman = 5
multi_troop_class_mounted_archer = 6
multi_troop_class_mounted_crossbowman = 7

multi_num_valid_entry_points = 64
multi_num_valid_entry_points_div_2 = 32

#normal money management system
multi_battle_round_team_money_add = 500
multi_destroy_save_or_destroy_target_money_add = 100
multi_destroy_target_money_add = 1500
multi_initial_gold_value = 1000
multi_max_gold_that_can_be_stored = 15000

multi_killer_agent_standard_money_add = 150 #(2/3 = 100 for battle & destroy, 3/3 = 150 for siege, 4/3 = 200 for deathmatch/team deathmatch/capture the flag/headquarters)
multi_killer_agent_loot_percentage_share = 12 #(2/3 = 8% for battle & destroy, 3/3 = 12% for siege, 4/3 = 16% for deathmatch/team deathmatch/capture the flag/headquarters)
multi_dead_agent_loot_percentage_share = 48 #(2/3 = 32% for battle & destroy, 3/3 = 48% for siege, 4/3 = 64% for deathmatch/team deathmatch/capture the flag/headquarters)
multi_minimum_gold = 1000 #(same in all modes)

multi_minimum_target_health = 1200

multi_max_seconds_flag_can_stay_in_ground = 60

multi_capture_the_flag_score_flag_returning = 1

multi_initial_spawn_point_team_1 = 0
multi_initial_spawn_point_team_2 = 32
multi_base_point_team_1 = 64
multi_base_point_team_2 = 65
multi_siege_flag_point = 66
multi_death_mode_point = 67

multi_headquarters_pole_height = 900
multi_headquarters_flag_height_to_win = 800 #used in sd death mode
multi_headquarters_flag_initial_height = 100 #used in sd death mode
multi_headquarters_max_distance_sq_to_raise_flags = 1600 #4m * 4m * 100 = 1600
multi_headquarters_distance_sq_to_set_flag = 8100 #9m * 9m * 100 = 8100 
multi_headquarters_distance_sq_to_change_flag = 400 #2m * 2m * 100 = 400 
multi_headquarters_distance_to_change_flag = 200 #2m * 100 = 200 
multi_distance_sq_to_use_belfry = 36 #6m * 6m = 36 (there is no * 100 for this one because it uses get_sq_distance_between_positions_in_meters instead of get_sq_distance_between_positions)
multi_max_sq_dist_between_agents_to_longer_mof_time = 49 #7m * 7m = 49m
min_allowed_flag_height_difference_to_make_score = 50

#these two values are about when master of field will be kicked
multiplayer_battle_formula_value_a = 15
multiplayer_battle_formula_value_b = 18000 #think about 18000-20000 if death mod very much happens.

multiplayer_spawn_above_opt_enemy_dist_point = 32 #while finding most suitable spawn point if nearest enemy is further than 32 meters give negative points to that spawn point
multiplayer_spawn_min_enemy_dist_limit = 45 #while finding most suitable spawn point if nearest enemy is closer than 45 meters give negative points to that spawn point, (squared increase)

multiplayer_poll_disable_period = 900 #15 minutes

#menu variables
escape_menu_item_height = 40

spf_all_teams_are_enemy                      = 0x00000001, 
spf_is_horseman                              = 0x00000002,
spf_examine_all_spawn_points                 = 0x00000004,
spf_team_0_spawn_far_from_entry_32           = 0x00000008,
spf_team_1_spawn_far_from_entry_0            = 0x00000010,
spf_team_1_spawn_far_from_entry_66           = 0x00000020,
spf_team_0_spawn_near_entry_0                = 0x00000040,
spf_team_0_spawn_near_entry_66               = 0x00000080,
spf_team_1_spawn_near_entry_32               = 0x00000100,
spf_team_0_walkers_spawn_at_high_points      = 0x00000200,
spf_team_1_walkers_spawn_at_high_points      = 0x00000400,
spf_try_to_spawn_close_to_at_least_one_enemy = 0x00000800,
spf_care_agent_to_agent_distances_less       = 0x00001000,



bignum = 0x40000000000000000000000000000000

op_num_value_bits = 24 + 32

tag_register        =  1
tag_variable        =  2
tag_string          =  3
tag_item            =  4
tag_troop           =  5
tag_faction         =  6
tag_quest           =  7
tag_party_tpl       =  8
tag_party           =  9
tag_scene           = 10
tag_mission_tpl     = 11
tag_menu            = 12
tag_script          = 13
tag_particle_sys    = 14
tag_scene_prop      = 15
tag_sound           = 16
tag_local_variable  = 17
tag_map_icon        = 18
tag_skill           = 19
tag_mesh            = 20
tag_presentation    = 21
tag_quick_string    = 22
tag_track	    = 23
tag_tableau         = 24
tag_animation       = 25
tags_end            = 26


opmask_register             =  tag_register       << op_num_value_bits
opmask_variable             =  tag_variable       << op_num_value_bits
##opmask_string             =  tag_string         << op_num_value_bits
##opmask_item_index         =  tag_item           << op_num_value_bits
##opmask_troop_index        =  tag_troop          << op_num_value_bits
##opmask_faction_index      =  tag_faction        << op_num_value_bits
opmask_quest_index          =  tag_quest          << op_num_value_bits
##opmask_p_template_index   =  tag_party_tpl      << op_num_value_bits
##opmask_party_index        =  tag_party          << op_num_value_bits
##opmask_scene_index        =  tag_scene          << op_num_value_bits
##opmask_mission_tpl_index  =  tag_mission_tpl    << op_num_value_bits
##opmask_menu_index         =  tag_menu           << op_num_value_bits
##opmask_script             =  tag_script         << op_num_value_bits
##opmask_particle_sys       =  tag_particle_sys   << op_num_value_bits
##opmask_scene_prop         =  tag_scene_prop     << op_num_value_bits
##opmask_sound              =  tag_sound          << op_num_value_bits
##opmask_map_icon           =  tag_map_icon       << op_num_value_bits
opmask_local_variable       =  tag_local_variable << op_num_value_bits
opmask_quick_string         =  tag_quick_string   << op_num_value_bits

#Tooltip types
tooltip_agent = 1
tooltip_horse = 2
tooltip_my_horse = 3
tooltip_container = 5
tooltip_door = 6
tooltip_item = 7
tooltip_leave_area = 8
tooltip_prop = 9
tooltip_destructible_prop = 10

#Human bones
hb_abdomen = 0
hb_thigh_l = 1
hb_calf_l = 2
hb_foot_l = 3
hb_thigh_r = 4
hb_calf_r = 5
hb_foot_r = 6
hb_spine = 7
hb_thorax = 8
hb_head = 9
hb_shoulder_l = 10
hb_upperarm_l = 11
hb_forearm_l = 12
hb_hand_l = 13
hb_item_l = 14
hb_shoulder_r = 15
hb_upperarm_r = 16
hb_forearm_r = 17
hb_hand_r = 18
hb_item_r = 19

#Horse bones
hrsb_pelvis = 0
hrsb_spine_1 = 1
hrsb_spine_2 = 2
hrsb_spine_3 = 3
hrsb_neck_1 = 4
hrsb_neck_2 = 5
hrsb_neck_3 = 6
hrsb_head = 7
hrsb_l_clavicle = 8
hrsb_l_upper_arm = 9
hrsb_l_forearm = 10
hrsb_l_hand = 11
hrsb_l_front_hoof = 12
hrsb_r_clavicle = 13
hrsb_r_upper_arm = 14
hrsb_r_forearm = 15
hrsb_r_hand = 16
hrsb_r_front_hoof = 17
hrsb_l_thigh = 18
hrsb_l_calf = 19
hrsb_l_foot = 20
hrsb_l_back_hoof = 21
hrsb_r_thigh = 22
hrsb_r_calf = 23
hrsb_r_foot = 24
hrsb_r_back_hoof = 25
hrsb_tail_1 = 26
hrsb_tail_2 = 27

#Attack directions
atk_thrust = 0
atk_right_swing = 1
atk_left_swing = 2
atk_overhead = 3

#Game windows
window_inventory = 7
window_party = 8
window_character = 11

#Agent body meta meshes
bmm_head = 0
bmm_beard = 1
bmm_hair = 2
bmm_helmet = 3
bmm_armor = 4
bmm_trousers = 5
bmm_left_foot = 6
bmm_right_foot = 7
bmm_armature = 8
bmm_item_1 = 9
bmm_item_2 = 10
bmm_item_3 = 11
bmm_item_4 = 12
bmm_missile_1 = 13
bmm_missile_2 = 14
bmm_missile_3 = 15
bmm_missile_4 = 16
bmm_carry_1 = 17
bmm_carry_2 = 18
bmm_carry_3 = 19
bmm_carry_4 = 20
bmm_unknown_2 = 21
bmm_left_hand = 22
bmm_right_hand = 23
bmm_left_bracer = 24
bmm_right_bracer = 25
bmm_banner = 26
bmm_name = 27

#Floating point registers
fp0 = 0
fp1 = 1
fp2 = 2
fp3 = 3
fp4 = 4
fp5 = 5
fp6 = 6
fp7 = 7
fp8 = 8
fp9 = 9
fp10 = 10
fp11 = 11
fp12 = 12
fp13 = 13
fp14 = 14
fp15 = 15
fp16 = 16
fp17 = 17
fp18 = 18
fp19 = 19
fp20 = 20
fp21 = 21
fp22 = 22
fp23 = 23
fp24 = 24
fp25 = 25
fp26 = 26
fp27 = 27
fp28 = 28
fp29 = 29
fp30 = 30
fp31 = 31
fp32 = 32
fp33 = 33
fp34 = 34
fp35 = 35
fp36 = 36
fp37 = 37
fp38 = 38
fp39 = 39
fp40 = 40
fp41 = 41
fp42 = 42
fp43 = 43
fp44 = 44
fp45 = 45
fp46 = 46
fp47 = 47
fp48 = 48
fp49 = 49
fp50 = 50
fp51 = 51
fp52 = 52
fp53 = 53
fp54 = 54
fp55 = 55
fp56 = 56
fp57 = 57
fp58 = 58
fp59 = 59
fp60 = 60
fp61 = 61
fp62 = 62
fp63 = 63
fp64 = 64
fp65 = 65
fp66 = 66
fp67 = 67
fp68 = 68
fp69 = 69
fp70 = 70
fp71 = 71
fp72 = 72
fp73 = 73
fp74 = 74
fp75 = 75
fp76 = 76
fp77 = 77
fp78 = 78
fp79 = 79
fp80 = 80
fp81 = 81
fp82 = 82
fp83 = 83
fp84 = 84
fp85 = 85
fp86 = 86
fp87 = 87
fp88 = 88
fp89 = 89
fp90 = 90
fp91 = 91
fp92 = 92
fp93 = 93
fp94 = 94
fp95 = 95
fp96 = 96
fp97 = 97
fp98 = 98
fp99 = 99
fp100 = 100
fp101 = 101
fp102 = 102
fp103 = 103
fp104 = 104
fp105 = 105
fp106 = 106
fp107 = 107
fp108 = 108
fp109 = 109
fp110 = 110
fp111 = 111
fp112 = 112
fp113 = 113
fp114 = 114
fp115 = 115
fp116 = 116
fp117 = 117
fp118 = 118
fp119 = 119
fp120 = 120
fp121 = 121
fp122 = 122
fp123 = 123
fp124 = 124
fp125 = 125
fp126 = 126
fp127 = 127


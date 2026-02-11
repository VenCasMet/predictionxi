import os
import pandas as pd

def load_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "data", "FullData.csv")
    return pd.read_csv(file_path)


# Calculate all role scores
def calculate_scores(df):
    a, b, c, d = 0.5, 1, 2, 3

    # Goalkeepers
    df['gk_Shot_Stopper'] = (
        b*df.Reactions + b*df.Composure + a*df.Speed + a*df.Strength +
        c*df.Jumping + b*df.GK_Positioning + c*df.GK_Diving +
        d*df.GK_Reflexes + b*df.GK_Handling
    ) / (2*a + 4*b + 2*c + 1*d)

    # Defenders
    df['df_score'] = (
        d*df.Reactions + c*df.Interceptions +
        d*df.Sliding_Tackle + d*df.Standing_Tackle +
        d*df.Marking + d*df.Heading +
        c*df.Aggression + c*df.Jumping
    ) / (4*d + 3*c)

    # Midfielders
    df['mf_score'] = (
        d*df.Ball_Control + d*df.Dribbling +
        d*df.Vision + d*df.Short_Pass +
        c*df.Long_Pass + c*df.Composure
    ) / (4*d + 2*c)

    # Attackers
    df['att_score'] = (
        d*df.Finishing + d*df.Heading +
        c*df.Dribbling + c*df.Ball_Control +
        c*df.Acceleration + c*df.Speed
    ) / (2*d + 4*c)

    return df


# Generate team based on formation
def generate_team(formation: str):

    df = load_data()
    df = calculate_scores(df)

    formations = {
        "4-3-3": (4, 3, 3),
        "4-4-2": (4, 4, 2),
        "3-5-2": (3, 5, 2),
        "4-2-3-1": (4, 5, 1)
    }

    if formation not in formations:
        return {"error": "Invalid formation"}

    defenders_needed, midfielders_needed, attackers_needed = formations[formation]

    # Goalkeeper
    gk = df[df['Club_Position'] == 'GK'] \
        .sort_values('gk_Shot_Stopper', ascending=False) \
        .head(1)

    # Defenders
    defender_positions = ['CB','LCB','RCB','LB','RB','LWB','RWB']
    defenders = df[df['Club_Position'].isin(defender_positions)] \
        .sort_values('df_score', ascending=False) \
        .head(defenders_needed)

    # Midfielders
    midfielder_positions = ['CM','LCM','RCM','CAM','CDM','LM','RM']
    midfielders = df[df['Club_Position'].isin(midfielder_positions)] \
        .sort_values('mf_score', ascending=False) \
        .head(midfielders_needed)

    # Attackers
    attacker_positions = ['ST','LW','RW','CF','LS','RS']
    attackers = df[df['Club_Position'].isin(attacker_positions)] \
        .sort_values('att_score', ascending=False) \
        .head(attackers_needed)

    return {
        "goalkeeper": gk['Name'].tolist(),
        "defenders": defenders['Name'].tolist(),
        "midfielders": midfielders['Name'].tolist(),
        "attackers": attackers['Name'].tolist()
    }
